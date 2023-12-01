;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::my_info)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'my_info (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::MY_INFO")
  (make-package "BEGINNER_TUTORIALS::MY_INFO"))

(in-package "ROS")
;;//! \htmlinclude my_info.msg.html


(defclass beginner_tutorials::my_info
  :super ros::object
  :slots (_name _height _weight ))

(defmethod beginner_tutorials::my_info
  (:init
   (&key
    ((:name __name) "")
    ((:height __height) 0.0)
    ((:weight __weight) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _height (float __height))
   (setq _weight (float __weight))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:weight
   (&optional __weight)
   (if __weight (setq _weight __weight)) _weight)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; float32 _height
    4
    ;; float32 _weight
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _weight
       (sys::poke _weight (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _weight
     (setq _weight (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get beginner_tutorials::my_info :md5sum-) "f8b3f5b2c4ae2022214645498883c09b")
(setf (get beginner_tutorials::my_info :datatype-) "beginner_tutorials/my_info")
(setf (get beginner_tutorials::my_info :definition-)
      "string name
float32 height
float32 weight
")



(provide :beginner_tutorials/my_info "f8b3f5b2c4ae2022214645498883c09b")


