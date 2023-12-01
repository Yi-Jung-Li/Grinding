;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::Ask_img)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'Ask_img (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::ASK_IMG")
  (make-package "TM_MSGS::ASK_IMG"))
(unless (find-package "TM_MSGS::ASK_IMGREQUEST")
  (make-package "TM_MSGS::ASK_IMGREQUEST"))
(unless (find-package "TM_MSGS::ASK_IMGRESPONSE")
  (make-package "TM_MSGS::ASK_IMGRESPONSE"))

(in-package "ROS")





(defclass tm_msgs::Ask_imgRequest
  :super ros::object
  :slots (_file_name ))

(defmethod tm_msgs::Ask_imgRequest
  (:init
   (&key
    ((:file_name __file_name) "")
    )
   (send-super :init)
   (setq _file_name (string __file_name))
   self)
  (:file_name
   (&optional __file_name)
   (if __file_name (setq _file_name __file_name)) _file_name)
  (:serialization-length
   ()
   (+
    ;; string _file_name
    4 (length _file_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _file_name
       (write-long (length _file_name) s) (princ _file_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _file_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _file_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass tm_msgs::Ask_imgResponse
  :super ros::object
  :slots (_ok _error ))

(defmethod tm_msgs::Ask_imgResponse
  (:init
   (&key
    ((:ok __ok) nil)
    ((:error __error) "")
    )
   (send-super :init)
   (setq _ok __ok)
   (setq _error (string __error))
   self)
  (:ok
   (&optional __ok)
   (if __ok (setq _ok __ok)) _ok)
  (:error
   (&optional __error)
   (if __error (setq _error __error)) _error)
  (:serialization-length
   ()
   (+
    ;; bool _ok
    1
    ;; string _error
    4 (length _error)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _ok
       (if _ok (write-byte -1 s) (write-byte 0 s))
     ;; string _error
       (write-long (length _error) s) (princ _error s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _ok
     (setq _ok (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _error
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _error (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass tm_msgs::Ask_img
  :super ros::object
  :slots ())

(setf (get tm_msgs::Ask_img :md5sum-) "dc18f33ad8fd47637626ae0ea2c4eb17")
(setf (get tm_msgs::Ask_img :datatype-) "tm_msgs/Ask_img")
(setf (get tm_msgs::Ask_img :request) tm_msgs::Ask_imgRequest)
(setf (get tm_msgs::Ask_img :response) tm_msgs::Ask_imgResponse)

(defmethod tm_msgs::Ask_imgRequest
  (:response () (instance tm_msgs::Ask_imgResponse :init)))

(setf (get tm_msgs::Ask_imgRequest :md5sum-) "dc18f33ad8fd47637626ae0ea2c4eb17")
(setf (get tm_msgs::Ask_imgRequest :datatype-) "tm_msgs/Ask_imgRequest")
(setf (get tm_msgs::Ask_imgRequest :definition-)
      "string file_name
---
bool ok
string error

")

(setf (get tm_msgs::Ask_imgResponse :md5sum-) "dc18f33ad8fd47637626ae0ea2c4eb17")
(setf (get tm_msgs::Ask_imgResponse :datatype-) "tm_msgs/Ask_imgResponse")
(setf (get tm_msgs::Ask_imgResponse :definition-)
      "string file_name
---
bool ok
string error

")



(provide :tm_msgs/Ask_img "dc18f33ad8fd47637626ae0ea2c4eb17")


