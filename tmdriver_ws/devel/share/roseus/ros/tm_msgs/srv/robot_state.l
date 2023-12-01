;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::robot_state)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'robot_state (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::ROBOT_STATE")
  (make-package "TM_MSGS::ROBOT_STATE"))
(unless (find-package "TM_MSGS::ROBOT_STATEREQUEST")
  (make-package "TM_MSGS::ROBOT_STATEREQUEST"))
(unless (find-package "TM_MSGS::ROBOT_STATERESPONSE")
  (make-package "TM_MSGS::ROBOT_STATERESPONSE"))

(in-package "ROS")





(defclass tm_msgs::robot_stateRequest
  :super ros::object
  :slots (_state ))

(defmethod tm_msgs::robot_stateRequest
  (:init
   (&key
    ((:state __state) 0)
    )
   (send-super :init)
   (setq _state (round __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; int8 _state
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _state
       (write-byte _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _state
     (setq _state (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _state 127) (setq _state (- _state 256)))
   ;;
   self)
  )

(defclass tm_msgs::robot_stateResponse
  :super ros::object
  :slots (_joint_state _end_effect ))

(defmethod tm_msgs::robot_stateResponse
  (:init
   (&key
    ((:joint_state __joint_state) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:end_effect __end_effect) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _joint_state __joint_state)
   (setq _end_effect __end_effect)
   self)
  (:joint_state
   (&optional __joint_state)
   (if __joint_state (setq _joint_state __joint_state)) _joint_state)
  (:end_effect
   (&optional __end_effect)
   (if __end_effect (setq _end_effect __end_effect)) _end_effect)
  (:serialization-length
   ()
   (+
    ;; float64[] _joint_state
    (* 8    (length _joint_state)) 4
    ;; float64[] _end_effect
    (* 8    (length _end_effect)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _joint_state
     (write-long (length _joint_state) s)
     (dotimes (i (length _joint_state))
       (sys::poke (elt _joint_state i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _end_effect
     (write-long (length _end_effect) s)
     (dotimes (i (length _end_effect))
       (sys::poke (elt _end_effect i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _joint_state
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joint_state (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _joint_state i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _end_effect
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _end_effect (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _end_effect i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass tm_msgs::robot_state
  :super ros::object
  :slots ())

(setf (get tm_msgs::robot_state :md5sum-) "8179a08027057ba6ad3ae82542746bab")
(setf (get tm_msgs::robot_state :datatype-) "tm_msgs/robot_state")
(setf (get tm_msgs::robot_state :request) tm_msgs::robot_stateRequest)
(setf (get tm_msgs::robot_state :response) tm_msgs::robot_stateResponse)

(defmethod tm_msgs::robot_stateRequest
  (:response () (instance tm_msgs::robot_stateResponse :init)))

(setf (get tm_msgs::robot_stateRequest :md5sum-) "8179a08027057ba6ad3ae82542746bab")
(setf (get tm_msgs::robot_stateRequest :datatype-) "tm_msgs/robot_stateRequest")
(setf (get tm_msgs::robot_stateRequest :definition-)
      "int8 state
---
float64[] joint_state
float64[] end_effect 

")

(setf (get tm_msgs::robot_stateResponse :md5sum-) "8179a08027057ba6ad3ae82542746bab")
(setf (get tm_msgs::robot_stateResponse :datatype-) "tm_msgs/robot_stateResponse")
(setf (get tm_msgs::robot_stateResponse :definition-)
      "int8 state
---
float64[] joint_state
float64[] end_effect 

")



(provide :tm_msgs/robot_state "8179a08027057ba6ad3ae82542746bab")


