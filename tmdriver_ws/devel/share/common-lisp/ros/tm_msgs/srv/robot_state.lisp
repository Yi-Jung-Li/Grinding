; Auto-generated. Do not edit!


(cl:in-package tm_msgs-srv)


;//! \htmlinclude robot_state-request.msg.html

(cl:defclass <robot_state-request> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0))
)

(cl:defclass robot_state-request (<robot_state-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_state-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_state-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<robot_state-request> is deprecated: use tm_msgs-srv:robot_state-request instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <robot_state-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:state-val is deprecated.  Use tm_msgs-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_state-request>) ostream)
  "Serializes a message object of type '<robot_state-request>"
  (cl:let* ((signed (cl:slot-value msg 'state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_state-request>) istream)
  "Deserializes a message object of type '<robot_state-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_state-request>)))
  "Returns string type for a service object of type '<robot_state-request>"
  "tm_msgs/robot_stateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_state-request)))
  "Returns string type for a service object of type 'robot_state-request"
  "tm_msgs/robot_stateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_state-request>)))
  "Returns md5sum for a message object of type '<robot_state-request>"
  "8179a08027057ba6ad3ae82542746bab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_state-request)))
  "Returns md5sum for a message object of type 'robot_state-request"
  "8179a08027057ba6ad3ae82542746bab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_state-request>)))
  "Returns full string definition for message of type '<robot_state-request>"
  (cl:format cl:nil "int8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_state-request)))
  "Returns full string definition for message of type 'robot_state-request"
  (cl:format cl:nil "int8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_state-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_state-request>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_state-request
    (cl:cons ':state (state msg))
))
;//! \htmlinclude robot_state-response.msg.html

(cl:defclass <robot_state-response> (roslisp-msg-protocol:ros-message)
  ((joint_state
    :reader joint_state
    :initarg :joint_state
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (end_effect
    :reader end_effect
    :initarg :end_effect
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass robot_state-response (<robot_state-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <robot_state-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'robot_state-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<robot_state-response> is deprecated: use tm_msgs-srv:robot_state-response instead.")))

(cl:ensure-generic-function 'joint_state-val :lambda-list '(m))
(cl:defmethod joint_state-val ((m <robot_state-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:joint_state-val is deprecated.  Use tm_msgs-srv:joint_state instead.")
  (joint_state m))

(cl:ensure-generic-function 'end_effect-val :lambda-list '(m))
(cl:defmethod end_effect-val ((m <robot_state-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:end_effect-val is deprecated.  Use tm_msgs-srv:end_effect instead.")
  (end_effect m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <robot_state-response>) ostream)
  "Serializes a message object of type '<robot_state-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'joint_state))))
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
   (cl:slot-value msg 'joint_state))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'end_effect))))
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
   (cl:slot-value msg 'end_effect))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <robot_state-response>) istream)
  "Deserializes a message object of type '<robot_state-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'joint_state) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'joint_state)))
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
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'end_effect) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'end_effect)))
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<robot_state-response>)))
  "Returns string type for a service object of type '<robot_state-response>"
  "tm_msgs/robot_stateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_state-response)))
  "Returns string type for a service object of type 'robot_state-response"
  "tm_msgs/robot_stateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<robot_state-response>)))
  "Returns md5sum for a message object of type '<robot_state-response>"
  "8179a08027057ba6ad3ae82542746bab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'robot_state-response)))
  "Returns md5sum for a message object of type 'robot_state-response"
  "8179a08027057ba6ad3ae82542746bab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<robot_state-response>)))
  "Returns full string definition for message of type '<robot_state-response>"
  (cl:format cl:nil "float64[] joint_state~%float64[] end_effect ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'robot_state-response)))
  "Returns full string definition for message of type 'robot_state-response"
  (cl:format cl:nil "float64[] joint_state~%float64[] end_effect ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <robot_state-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'joint_state) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'end_effect) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <robot_state-response>))
  "Converts a ROS message object to a list"
  (cl:list 'robot_state-response
    (cl:cons ':joint_state (joint_state msg))
    (cl:cons ':end_effect (end_effect msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'robot_state)))
  'robot_state-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'robot_state)))
  'robot_state-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'robot_state)))
  "Returns string type for a service object of type '<robot_state>"
  "tm_msgs/robot_state")