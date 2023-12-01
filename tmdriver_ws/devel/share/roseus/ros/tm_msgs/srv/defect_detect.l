;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::defect_detect)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'defect_detect (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::DEFECT_DETECT")
  (make-package "TM_MSGS::DEFECT_DETECT"))
(unless (find-package "TM_MSGS::DEFECT_DETECTREQUEST")
  (make-package "TM_MSGS::DEFECT_DETECTREQUEST"))
(unless (find-package "TM_MSGS::DEFECT_DETECTRESPONSE")
  (make-package "TM_MSGS::DEFECT_DETECTRESPONSE"))

(in-package "ROS")





(defclass tm_msgs::defect_detectRequest
  :super ros::object
  :slots (_function ))

(defmethod tm_msgs::defect_detectRequest
  (:init
   (&key
    ((:function __function) "")
    )
   (send-super :init)
   (setq _function (string __function))
   self)
  (:function
   (&optional __function)
   (if __function (setq _function __function)) _function)
  (:serialization-length
   ()
   (+
    ;; string _function
    4 (length _function)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _function
       (write-long (length _function) s) (princ _function s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _function
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _function (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass tm_msgs::defect_detectResponse
  :super ros::object
  :slots (_ok ))

(defmethod tm_msgs::defect_detectResponse
  (:init
   (&key
    ((:ok __ok) nil)
    )
   (send-super :init)
   (setq _ok __ok)
   self)
  (:ok
   (&optional __ok)
   (if __ok (setq _ok __ok)) _ok)
  (:serialization-length
   ()
   (+
    ;; bool _ok
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _ok
       (if _ok (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _ok
     (setq _ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass tm_msgs::defect_detect
  :super ros::object
  :slots ())

(setf (get tm_msgs::defect_detect :md5sum-) "bcee4f588ea52289bf77bc6d6629f851")
(setf (get tm_msgs::defect_detect :datatype-) "tm_msgs/defect_detect")
(setf (get tm_msgs::defect_detect :request) tm_msgs::defect_detectRequest)
(setf (get tm_msgs::defect_detect :response) tm_msgs::defect_detectResponse)

(defmethod tm_msgs::defect_detectRequest
  (:response () (instance tm_msgs::defect_detectResponse :init)))

(setf (get tm_msgs::defect_detectRequest :md5sum-) "bcee4f588ea52289bf77bc6d6629f851")
(setf (get tm_msgs::defect_detectRequest :datatype-) "tm_msgs/defect_detectRequest")
(setf (get tm_msgs::defect_detectRequest :definition-)
      "string function 
---
bool ok

")

(setf (get tm_msgs::defect_detectResponse :md5sum-) "bcee4f588ea52289bf77bc6d6629f851")
(setf (get tm_msgs::defect_detectResponse :datatype-) "tm_msgs/defect_detectResponse")
(setf (get tm_msgs::defect_detectResponse :definition-)
      "string function 
---
bool ok

")



(provide :tm_msgs/defect_detect "bcee4f588ea52289bf77bc6d6629f851")


