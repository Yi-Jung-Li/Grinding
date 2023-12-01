;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::ask_BMI)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'ask_BMI (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::ASK_BMI")
  (make-package "BEGINNER_TUTORIALS::ASK_BMI"))
(unless (find-package "BEGINNER_TUTORIALS::ASK_BMIREQUEST")
  (make-package "BEGINNER_TUTORIALS::ASK_BMIREQUEST"))
(unless (find-package "BEGINNER_TUTORIALS::ASK_BMIRESPONSE")
  (make-package "BEGINNER_TUTORIALS::ASK_BMIRESPONSE"))

(in-package "ROS")





(defclass beginner_tutorials::ask_BMIRequest
  :super ros::object
  :slots (_height _weight ))

(defmethod beginner_tutorials::ask_BMIRequest
  (:init
   (&key
    ((:height __height) 0.0)
    ((:weight __weight) 0.0)
    )
   (send-super :init)
   (setq _height (float __height))
   (setq _weight (float __weight))
   self)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:weight
   (&optional __weight)
   (if __weight (setq _weight __weight)) _weight)
  (:serialization-length
   ()
   (+
    ;; float32 _height
    4
    ;; float32 _weight
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _weight
       (sys::poke _weight (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _weight
     (setq _weight (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass beginner_tutorials::ask_BMIResponse
  :super ros::object
  :slots (_BMI ))

(defmethod beginner_tutorials::ask_BMIResponse
  (:init
   (&key
    ((:BMI __BMI) 0.0)
    )
   (send-super :init)
   (setq _BMI (float __BMI))
   self)
  (:BMI
   (&optional __BMI)
   (if __BMI (setq _BMI __BMI)) _BMI)
  (:serialization-length
   ()
   (+
    ;; float32 _BMI
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _BMI
       (sys::poke _BMI (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _BMI
     (setq _BMI (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass beginner_tutorials::ask_BMI
  :super ros::object
  :slots ())

(setf (get beginner_tutorials::ask_BMI :md5sum-) "3de0e12df6c14255537cca18d991ce8d")
(setf (get beginner_tutorials::ask_BMI :datatype-) "beginner_tutorials/ask_BMI")
(setf (get beginner_tutorials::ask_BMI :request) beginner_tutorials::ask_BMIRequest)
(setf (get beginner_tutorials::ask_BMI :response) beginner_tutorials::ask_BMIResponse)

(defmethod beginner_tutorials::ask_BMIRequest
  (:response () (instance beginner_tutorials::ask_BMIResponse :init)))

(setf (get beginner_tutorials::ask_BMIRequest :md5sum-) "3de0e12df6c14255537cca18d991ce8d")
(setf (get beginner_tutorials::ask_BMIRequest :datatype-) "beginner_tutorials/ask_BMIRequest")
(setf (get beginner_tutorials::ask_BMIRequest :definition-)
      "float32 height
float32 weight
---
float32 BMI

")

(setf (get beginner_tutorials::ask_BMIResponse :md5sum-) "3de0e12df6c14255537cca18d991ce8d")
(setf (get beginner_tutorials::ask_BMIResponse :datatype-) "beginner_tutorials/ask_BMIResponse")
(setf (get beginner_tutorials::ask_BMIResponse :definition-)
      "float32 height
float32 weight
---
float32 BMI

")



(provide :beginner_tutorials/ask_BMI "3de0e12df6c14255537cca18d991ce8d")


