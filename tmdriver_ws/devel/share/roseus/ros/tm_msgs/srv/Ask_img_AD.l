;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::Ask_img_AD)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'Ask_img_AD (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::ASK_IMG_AD")
  (make-package "TM_MSGS::ASK_IMG_AD"))
(unless (find-package "TM_MSGS::ASK_IMG_ADREQUEST")
  (make-package "TM_MSGS::ASK_IMG_ADREQUEST"))
(unless (find-package "TM_MSGS::ASK_IMG_ADRESPONSE")
  (make-package "TM_MSGS::ASK_IMG_ADRESPONSE"))

(in-package "ROS")





(defclass tm_msgs::Ask_img_ADRequest
  :super ros::object
  :slots (_file_path ))

(defmethod tm_msgs::Ask_img_ADRequest
  (:init
   (&key
    ((:file_path __file_path) "")
    )
   (send-super :init)
   (setq _file_path (string __file_path))
   self)
  (:file_path
   (&optional __file_path)
   (if __file_path (setq _file_path __file_path)) _file_path)
  (:serialization-length
   ()
   (+
    ;; string _file_path
    4 (length _file_path)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _file_path
       (write-long (length _file_path) s) (princ _file_path s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _file_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _file_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass tm_msgs::Ask_img_ADResponse
  :super ros::object
  :slots (_anomaly_score ))

(defmethod tm_msgs::Ask_img_ADResponse
  (:init
   (&key
    ((:anomaly_score __anomaly_score) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _anomaly_score __anomaly_score)
   self)
  (:anomaly_score
   (&optional __anomaly_score)
   (if __anomaly_score (setq _anomaly_score __anomaly_score)) _anomaly_score)
  (:serialization-length
   ()
   (+
    ;; float64[] _anomaly_score
    (* 8    (length _anomaly_score)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _anomaly_score
     (write-long (length _anomaly_score) s)
     (dotimes (i (length _anomaly_score))
       (sys::poke (elt _anomaly_score i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _anomaly_score
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _anomaly_score (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _anomaly_score i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass tm_msgs::Ask_img_AD
  :super ros::object
  :slots ())

(setf (get tm_msgs::Ask_img_AD :md5sum-) "718c3a88dd0f5e8414a94bc17ba46265")
(setf (get tm_msgs::Ask_img_AD :datatype-) "tm_msgs/Ask_img_AD")
(setf (get tm_msgs::Ask_img_AD :request) tm_msgs::Ask_img_ADRequest)
(setf (get tm_msgs::Ask_img_AD :response) tm_msgs::Ask_img_ADResponse)

(defmethod tm_msgs::Ask_img_ADRequest
  (:response () (instance tm_msgs::Ask_img_ADResponse :init)))

(setf (get tm_msgs::Ask_img_ADRequest :md5sum-) "718c3a88dd0f5e8414a94bc17ba46265")
(setf (get tm_msgs::Ask_img_ADRequest :datatype-) "tm_msgs/Ask_img_ADRequest")
(setf (get tm_msgs::Ask_img_ADRequest :definition-)
      "string file_path
---
float64[] anomaly_score 

")

(setf (get tm_msgs::Ask_img_ADResponse :md5sum-) "718c3a88dd0f5e8414a94bc17ba46265")
(setf (get tm_msgs::Ask_img_ADResponse :datatype-) "tm_msgs/Ask_img_ADResponse")
(setf (get tm_msgs::Ask_img_ADResponse :definition-)
      "string file_path
---
float64[] anomaly_score 

")



(provide :tm_msgs/Ask_img_AD "718c3a88dd0f5e8414a94bc17ba46265")


