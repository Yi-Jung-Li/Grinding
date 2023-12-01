# coding=utf-8

import os
import PySpin
import rospy
import sys
import cv2 
import numpy as np
from math import sin, pi, cos, ceil
from tm_msgs.srv import Ask_img
from tm_msgs.srv import Ask_imgResponse

def Crop(img, scale_factor=1.0, Origin_R=933):
    '''
    Parameters
    ----------
    img : ndarray
        Image Data

    scale_factor : float
        Resize scale for visualize

    Returns
    -------
    CropImg : ndarray
        Cropped Image
    '''

    # Resize
    img = cv2.resize(img,None,fx=scale_factor,fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    
    # Img Info
    h, w = img.shape[:2]
    ctr_x = int(w/2) + 1    # offset
    ctr_y = int(h/2) + 7

    # Radius of circle which in the image
    r = int(Origin_R * scale_factor)

    # Crop img's Rectangle params
    Rec_H_half = ceil(r * sin(45*pi/180))
    Rec_W_half = Rec_H_half
    x1 = ctr_x - Rec_W_half
    y1 = ctr_y - Rec_H_half
    x2 = ctr_x + Rec_W_half
    y2 = ctr_y + Rec_H_half

    # Crop image
    CropImg = img[y1:y2, x1:x2]

    return CropImg

def acquire_images(cam, nodemap, nodemap_tldevice, file_name):
    error_msg = 'No error'
    try:
        result = True
        # In order to access the node entries, they have to be casted to a pointer type (CEnumerationPtr here)
        node_acquisition_mode = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
        if not PySpin.IsAvailable(node_acquisition_mode) or not PySpin.IsWritable(node_acquisition_mode):
            print('Unable to set acquisition mode to continuous (enum retrieval). Aborting...')
            error_msg = 'Unable to set acquisition mode to continuous (enum retrieval). Aborting...'
            return False, error_msg

        # Retrieve entry node from enumeration node
        node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
        if not PySpin.IsAvailable(node_acquisition_mode_continuous) or not PySpin.IsReadable(node_acquisition_mode_continuous):
            print('Unable to set acquisition mode to continuous (entry retrieval). Aborting...')
            error_msg = 'Unable to set acquisition mode to continuous (entry retrieval). Aborting...'
            return False, error_msg

        # Retrieve integer value from entry node
        acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()

        # Set integer value from entry node as new value of enumeration node
        node_acquisition_mode.SetIntValue(acquisition_mode_continuous)

        print('Acquisition mode set to continuous...')
        cam.BeginAcquisition()
        print('Acquiring images...')

        device_serial_number = ''
        node_device_serial_number = PySpin.CStringPtr(nodemap_tldevice.GetNode('DeviceSerialNumber'))
        if PySpin.IsAvailable(node_device_serial_number) and PySpin.IsReadable(node_device_serial_number):
            device_serial_number = node_device_serial_number.GetValue()
            print('Device serial number retrieved as %s...' % device_serial_number)
        
        # Retrieve, convert, and save images
        try:
            image_result = cam.GetNextImage()
            if image_result.IsIncomplete():
                print('Image incomplete with image status %d ...' % image_result.GetImageStatus())
            
            else:
                i = 0
                width = image_result.GetWidth()
                height = image_result.GetHeight()
                print('Grabbed Image, width = %d, height = %d' % (width, height))
                image_converted = image_result.Convert(PySpin.PixelFormat_RGB8, PySpin.HQ_LINEAR)
                BGR_Img = image_converted.GetData().reshape(height, width, 3)
                RGB_Img = BGR_Img[:,:,::-1]

                # Crop image
                Crop_Img = Crop(RGB_Img, 1.0, Origin_R=925)
                ImgName = file_name+'.jpg'
                cv2.imwrite(ImgName, RGB_Img)
                ImgName = file_name+'_crop'+'.jpg'
                cv2.imwrite(ImgName, Crop_Img)
                print('Image saved at %s' % ImgName)
                image_result.Release()
                print('')

        except PySpin.SpinnakerException as ex:
            print('Error: %s' % ex)
            return False , ex
        cam.EndAcquisition()
        
    except PySpin.SpinnakerException as ex:
        print('Error: %s' % ex)
        return False, ex

    return result, error_msg


def acquire_one_images(req):
    error_msg = None
    result = True
    file_name = req.file_name
    # Acquire images
    result, error_msg = acquire_images(cam, nodemap, nodemap_tldevice, file_name)
    return Ask_imgResponse(result,error_msg)


# Retrieve singleton reference to system object
system = PySpin.System.GetInstance()

# Get current library version
version = system.GetLibraryVersion()
print('Library version: %d.%d.%d.%d' % (version.major, version.minor, version.type, version.build))

# Retrieve list of cameras from the system
cam_list = system.GetCameras()

num_cameras = cam_list.GetSize()

print('Number of cameras detected: %d' % num_cameras)

# Finish if there are no cameras
if num_cameras == 0:

    # Clear camera list before releasing system
    cam_list.Clear()

    # Release system instance
    system.ReleaseInstance()

    print('Not enough cameras!')
    input('Done! Press Enter to exit...')
    #return False
cam = cam_list[0]

try:
    result = True

    # Retrieve TL device nodemap and print device information
    nodemap_tldevice = cam.GetTLDeviceNodeMap()

    # Initialize camera
    cam.Init()

    cam.ExposureAuto.SetValue(PySpin.ExposureAuto_Off)
    # cam.BalanceWhiteAuto.SetValue(PySpin.BalanceWhiteAuto_Off)
    exposure_time_to_set = 70000.0
    exposure_time_to_set = min(cam.ExposureTime.GetMax(), exposure_time_to_set)
    cam.ExposureTime.SetValue(exposure_time_to_set)

    # Retrieve GenICam nodemap
    nodemap = cam.GetNodeMap()

except PySpin.SpinnakerException as ex:
    print('Error: %s' % ex)
    result = False


# Setup ros server and service
rospy.init_node('Camera_server',anonymous=True)
s = rospy.Service('Camera_service', Ask_img, acquire_one_images)
rospy.spin()

cam.DeInit()

# The usage of del is preferred to assigning the variable to None.
del cam

# Clear camera list before releasing system
cam_list.Clear()

# Release system instance
system.ReleaseInstance()

input('Done! Press Enter to exit...')


