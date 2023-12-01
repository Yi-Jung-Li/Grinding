;; Auto-generated. Do not edit!


(when (boundp 'tm_msgs::robot_motion)
  (if (not (find-package "TM_MSGS"))
    (make-package "TM_MSGS"))
  (shadow 'robot_motion (find-package "TM_MSGS")))
(unless (find-package "TM_MSGS::ROBOT_MOTION")
  (make-package "TM_MSGS::ROBOT_MOTION"))
(unless (find-package "TM_MSGS::ROBOT_MOTIONREQUEST")
  (make-package "TM_MSGS::ROBOT_MOTIONREQUEST"))
(unless (find-package "TM_MSGS::ROBOT_MOTIONRESPONSE")
  (make-package "TM_MSGS::ROBOT_MOTIONRESPONSE"))

(in-package "ROS")





(defclass tm_msgs::robot_motionRequest
  :super ros::object
  :slots (_goal_format _motion_type _goal _velocity_scaling_factor _constraints _plan_name _plan_index _move_to_plan_first_pose ))

(defmethod tm_msgs::robot_motionRequest
  (:init
   (&key
    ((:goal_format __goal_format) "")
    ((:motion_type __motion_type) "")
    ((:goal __goal) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:velocity_scaling_factor __velocity_scaling_factor) 0.0)
    ((:constraints __constraints) nil)
    ((:plan_name __plan_name) "")
    ((:plan_index __plan_index) 0)
    ((:move_to_plan_first_pose __move_to_plan_first_pose) nil)
    )
   (send-super :init)
   (setq _goal_format (string __goal_format))
   (setq _motion_type (string __motion_type))
   (setq _goal __goal)
   (setq _velocity_scaling_factor (float __velocity_scaling_factor))
   (setq _constraints __constraints)
   (setq _plan_name (string __plan_name))
   (setq _plan_index (round __plan_index))
   (setq _move_to_plan_first_pose __move_to_plan_first_pose)
   self)
  (:goal_format
   (&optional __goal_format)
   (if __goal_format (setq _goal_format __goal_format)) _goal_format)
  (:motion_type
   (&optional __motion_type)
   (if __motion_type (setq _motion_type __motion_type)) _motion_type)
  (:goal
   (&optional __goal)
   (if __goal (setq _goal __goal)) _goal)
  (:velocity_scaling_factor
   (&optional __velocity_scaling_factor)
   (if __velocity_scaling_factor (setq _velocity_scaling_factor __velocity_scaling_factor)) _velocity_scaling_factor)
  (:constraints
   (&optional __constraints)
   (if __constraints (setq _constraints __constraints)) _constraints)
  (:plan_name
   (&optional __plan_name)
   (if __plan_name (setq _plan_name __plan_name)) _plan_name)
  (:plan_index
   (&optional __plan_index)
   (if __plan_index (setq _plan_index __plan_index)) _plan_index)
  (:move_to_plan_first_pose
   (&optional __move_to_plan_first_pose)
   (if __move_to_plan_first_pose (setq _move_to_plan_first_pose __move_to_plan_first_pose)) _move_to_plan_first_pose)
  (:serialization-length
   ()
   (+
    ;; string _goal_format
    4 (length _goal_format)
    ;; string _motion_type
    4 (length _motion_type)
    ;; float64[] _goal
    (* 8    (length _goal)) 4
    ;; float64 _velocity_scaling_factor
    8
    ;; bool _constraints
    1
    ;; string _plan_name
    4 (length _plan_name)
    ;; int32 _plan_index
    4
    ;; bool _move_to_plan_first_pose
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _goal_format
       (write-long (length _goal_format) s) (princ _goal_format s)
     ;; string _motion_type
       (write-long (length _motion_type) s) (princ _motion_type s)
     ;; float64[] _goal
     (write-long (length _goal) s)
     (dotimes (i (length _goal))
       (sys::poke (elt _goal i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _velocity_scaling_factor
       (sys::poke _velocity_scaling_factor (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _constraints
       (if _constraints (write-byte -1 s) (write-byte 0 s))
     ;; string _plan_name
       (write-long (length _plan_name) s) (princ _plan_name s)
     ;; int32 _plan_index
       (write-long _plan_index s)
     ;; bool _move_to_plan_first_pose
       (if _move_to_plan_first_pose (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _goal_format
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _goal_format (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _motion_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motion_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64[] _goal
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _goal (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _goal i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _velocity_scaling_factor
     (setq _velocity_scaling_factor (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _constraints
     (setq _constraints (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _plan_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _plan_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _plan_index
     (setq _plan_index (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _move_to_plan_first_pose
     (setq _move_to_plan_first_pose (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass tm_msgs::robot_motionResponse
  :super ros::object
  :slots (_ok ))

(defmethod tm_msgs::robot_motionResponse
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

(defclass tm_msgs::robot_motion
  :super ros::object
  :slots ())

(setf (get tm_msgs::robot_motion :md5sum-) "8e3073766aab12c61a8c47f8c01da720")
(setf (get tm_msgs::robot_motion :datatype-) "tm_msgs/robot_motion")
(setf (get tm_msgs::robot_motion :request) tm_msgs::robot_motionRequest)
(setf (get tm_msgs::robot_motion :response) tm_msgs::robot_motionResponse)

(defmethod tm_msgs::robot_motionRequest
  (:response () (instance tm_msgs::robot_motionResponse :init)))

(setf (get tm_msgs::robot_motionRequest :md5sum-) "8e3073766aab12c61a8c47f8c01da720")
(setf (get tm_msgs::robot_motionRequest :datatype-) "tm_msgs/robot_motionRequest")
(setf (get tm_msgs::robot_motionRequest :definition-)
      "string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan 
string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan 
float64[] goal
float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]
bool constraints
string plan_name # file name of plan
int32 plan_index
bool move_to_plan_first_pose
---
bool ok

")

(setf (get tm_msgs::robot_motionResponse :md5sum-) "8e3073766aab12c61a8c47f8c01da720")
(setf (get tm_msgs::robot_motionResponse :datatype-) "tm_msgs/robot_motionResponse")
(setf (get tm_msgs::robot_motionResponse :definition-)
      "string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan 
string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan 
float64[] goal
float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]
bool constraints
string plan_name # file name of plan
int32 plan_index
bool move_to_plan_first_pose
---
bool ok

")



(provide :tm_msgs/robot_motion "8e3073766aab12c61a8c47f8c01da720")


