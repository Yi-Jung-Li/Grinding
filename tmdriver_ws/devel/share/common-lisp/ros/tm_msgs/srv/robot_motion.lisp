; Auto-generated. Do not edit!


(cl:in-package tm_msgs-srv)


;//! \htmlinclude robot_motion-request.msg.html

(cl:defclass <robot_motion-request> (roslisp-msg-protocol:ros-message)
  ((goal_format
    :reader goal_format
    :initarg :goal_format
    :type cl:string
    :initform "")
   (motion_type
    :reader motion_type
    :initarg :motion_type
    :type cl:string
    :initform "")
   (goal
    :reader goal
    :initarg :goal
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (velocity_scaling_factor
    :reader velocity_scaling_factor
    :initarg :velocity_scaling_factor
    :type cl:float
    :initform 0.0)
   (constraints
    :reader constraints
    :initarg :constraints
    :type cl:boolean
    :initform cl:nil)
   (plan_name
    :reader plan_name
    :initarg :plan_name
    :type cl:string
    :initform "")
   (plan_index
    :reader plan_index
    :initarg :plan_index
    :type cl:integer
    :initform 0)
   (move_to_plan_first_pose
    :reader move_to_plan_first_pose
    :initarg :move_to_plan_first_pose
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass robot_motion-request (<robot_motion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_motion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_motion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<robot_motion-request> is deprecated: use tm_msgs-srv:robot_motion-request instead.")))

(cl:ensure-generic-function 'goal_format-val :lambda-list '(m))
(cl:defmethod goal_format-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:goal_format-val is deprecated.  Use tm_msgs-srv:goal_format instead.")
  (goal_format m))

(cl:ensure-generic-function 'motion_type-val :lambda-list '(m))
(cl:defmethod motion_type-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:motion_type-val is deprecated.  Use tm_msgs-srv:motion_type instead.")
  (motion_type m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:goal-val is deprecated.  Use tm_msgs-srv:goal instead.")
  (goal m))

(cl:ensure-generic-function 'velocity_scaling_factor-val :lambda-list '(m))
(cl:defmethod velocity_scaling_factor-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:velocity_scaling_factor-val is deprecated.  Use tm_msgs-srv:velocity_scaling_factor instead.")
  (velocity_scaling_factor m))

(cl:ensure-generic-function 'constraints-val :lambda-list '(m))
(cl:defmethod constraints-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:constraints-val is deprecated.  Use tm_msgs-srv:constraints instead.")
  (constraints m))

(cl:ensure-generic-function 'plan_name-val :lambda-list '(m))
(cl:defmethod plan_name-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:plan_name-val is deprecated.  Use tm_msgs-srv:plan_name instead.")
  (plan_name m))

(cl:ensure-generic-function 'plan_index-val :lambda-list '(m))
(cl:defmethod plan_index-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:plan_index-val is deprecated.  Use tm_msgs-srv:plan_index instead.")
  (plan_index m))

(cl:ensure-generic-function 'move_to_plan_first_pose-val :lambda-list '(m))
(cl:defmethod move_to_plan_first_pose-val ((m <robot_motion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:move_to_plan_first_pose-val is deprecated.  Use tm_msgs-srv:move_to_plan_first_pose instead.")
  (move_to_plan_first_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_motion-request>) ostream)
  "Serializes a message object of type '<robot_motion-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_format))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_format))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'motion_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'motion_type))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'goal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'goal))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'velocity_scaling_factor))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'constraints) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'plan_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'plan_name))
  (cl:let* ((signed (cl:slot-value msg 'plan_index)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'move_to_plan_first_pose) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_motion-request>) istream)
  "Deserializes a message object of type '<robot_motion-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_format) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_format) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motion_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'motion_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'goal) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'goal)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity_scaling_factor) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'constraints) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'plan_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'plan_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'plan_index) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'move_to_plan_first_pose) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_motion-request>)))
  "Returns string type for a service object of type '<robot_motion-request>"
  "tm_msgs/robot_motionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_motion-request)))
  "Returns string type for a service object of type 'robot_motion-request"
  "tm_msgs/robot_motionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_motion-request>)))
  "Returns md5sum for a message object of type '<robot_motion-request>"
  "8e3073766aab12c61a8c47f8c01da720")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_motion-request)))
  "Returns md5sum for a message object of type 'robot_motion-request"
  "8e3073766aab12c61a8c47f8c01da720")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_motion-request>)))
  "Returns full string definition for message of type '<robot_motion-request>"
  (cl:format cl:nil "string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan ~%string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan ~%float64[] goal~%float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]~%bool constraints~%string plan_name # file name of plan~%int32 plan_index~%bool move_to_plan_first_pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_motion-request)))
  "Returns full string definition for message of type 'robot_motion-request"
  (cl:format cl:nil "string goal_format # 'JPP' or 'CPP' (Joint angle or Cartesian), 'plan' for excute certain plan ~%string motion_type # 'PTP' or 'line' , if goal_format is 'plan', motion_type will be the file path of plan ~%float64[] goal~%float64 velocity_scaling_factor # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]~%bool constraints~%string plan_name # file name of plan~%int32 plan_index~%bool move_to_plan_first_pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_motion-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'goal_format))
     4 (cl:length (cl:slot-value msg 'motion_type))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'goal) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     8
     1
     4 (cl:length (cl:slot-value msg 'plan_name))
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_motion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_motion-request
    (cl:cons ':goal_format (goal_format msg))
    (cl:cons ':motion_type (motion_type msg))
    (cl:cons ':goal (goal msg))
    (cl:cons ':velocity_scaling_factor (velocity_scaling_factor msg))
    (cl:cons ':constraints (constraints msg))
    (cl:cons ':plan_name (plan_name msg))
    (cl:cons ':plan_index (plan_index msg))
    (cl:cons ':move_to_plan_first_pose (move_to_plan_first_pose msg))
))
;//! \htmlinclude robot_motion-response.msg.html

(cl:defclass <robot_motion-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass robot_motion-response (<robot_motion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_motion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_motion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<robot_motion-response> is deprecated: use tm_msgs-srv:robot_motion-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <robot_motion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:ok-val is deprecated.  Use tm_msgs-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_motion-response>) ostream)
  "Serializes a message object of type '<robot_motion-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_motion-response>) istream)
  "Deserializes a message object of type '<robot_motion-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_motion-response>)))
  "Returns string type for a service object of type '<robot_motion-response>"
  "tm_msgs/robot_motionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_motion-response)))
  "Returns string type for a service object of type 'robot_motion-response"
  "tm_msgs/robot_motionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_motion-response>)))
  "Returns md5sum for a message object of type '<robot_motion-response>"
  "8e3073766aab12c61a8c47f8c01da720")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_motion-response)))
  "Returns md5sum for a message object of type 'robot_motion-response"
  "8e3073766aab12c61a8c47f8c01da720")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_motion-response>)))
  "Returns full string definition for message of type '<robot_motion-response>"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_motion-response)))
  "Returns full string definition for message of type 'robot_motion-response"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_motion-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_motion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_motion-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'robot_motion)))
  'robot_motion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'robot_motion)))
  'robot_motion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_motion)))
  "Returns string type for a service object of type '<robot_motion>"
  "tm_msgs/robot_motion")