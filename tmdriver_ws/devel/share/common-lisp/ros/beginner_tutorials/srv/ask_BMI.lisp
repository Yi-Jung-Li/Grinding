; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-srv)


;//! \htmlinclude ask_BMI-request.msg.html

(cl:defclass <ask_BMI-request> (roslisp-msg-protocol:ros-message)
  ((height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0)
   (weight
    :reader weight
    :initarg :weight
    :type cl:float
    :initform 0.0))
)

(cl:defclass ask_BMI-request (<ask_BMI-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ask_BMI-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ask_BMI-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<ask_BMI-request> is deprecated: use beginner_tutorials-srv:ask_BMI-request instead.")))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ask_BMI-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:height-val is deprecated.  Use beginner_tutorials-srv:height instead.")
  (height m))

(cl:ensure-generic-function 'weight-val :lambda-list '(m))
(cl:defmethod weight-val ((m <ask_BMI-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:weight-val is deprecated.  Use beginner_tutorials-srv:weight instead.")
  (weight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ask_BMI-request>) ostream)
  "Serializes a message object of type '<ask_BMI-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'weight))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ask_BMI-request>) istream)
  "Deserializes a message object of type '<ask_BMI-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'weight) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ask_BMI-request>)))
  "Returns string type for a service object of type '<ask_BMI-request>"
  "beginner_tutorials/ask_BMIRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ask_BMI-request)))
  "Returns string type for a service object of type 'ask_BMI-request"
  "beginner_tutorials/ask_BMIRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ask_BMI-request>)))
  "Returns md5sum for a message object of type '<ask_BMI-request>"
  "3de0e12df6c14255537cca18d991ce8d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ask_BMI-request)))
  "Returns md5sum for a message object of type 'ask_BMI-request"
  "3de0e12df6c14255537cca18d991ce8d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ask_BMI-request>)))
  "Returns full string definition for message of type '<ask_BMI-request>"
  (cl:format cl:nil "float32 height~%float32 weight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ask_BMI-request)))
  "Returns full string definition for message of type 'ask_BMI-request"
  (cl:format cl:nil "float32 height~%float32 weight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ask_BMI-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ask_BMI-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ask_BMI-request
    (cl:cons ':height (height msg))
    (cl:cons ':weight (weight msg))
))
;//! \htmlinclude ask_BMI-response.msg.html

(cl:defclass <ask_BMI-response> (roslisp-msg-protocol:ros-message)
  ((BMI
    :reader BMI
    :initarg :BMI
    :type cl:float
    :initform 0.0))
)

(cl:defclass ask_BMI-response (<ask_BMI-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ask_BMI-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ask_BMI-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<ask_BMI-response> is deprecated: use beginner_tutorials-srv:ask_BMI-response instead.")))

(cl:ensure-generic-function 'BMI-val :lambda-list '(m))
(cl:defmethod BMI-val ((m <ask_BMI-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:BMI-val is deprecated.  Use beginner_tutorials-srv:BMI instead.")
  (BMI m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ask_BMI-response>) ostream)
  "Serializes a message object of type '<ask_BMI-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'BMI))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ask_BMI-response>) istream)
  "Deserializes a message object of type '<ask_BMI-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'BMI) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ask_BMI-response>)))
  "Returns string type for a service object of type '<ask_BMI-response>"
  "beginner_tutorials/ask_BMIResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ask_BMI-response)))
  "Returns string type for a service object of type 'ask_BMI-response"
  "beginner_tutorials/ask_BMIResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ask_BMI-response>)))
  "Returns md5sum for a message object of type '<ask_BMI-response>"
  "3de0e12df6c14255537cca18d991ce8d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ask_BMI-response)))
  "Returns md5sum for a message object of type 'ask_BMI-response"
  "3de0e12df6c14255537cca18d991ce8d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ask_BMI-response>)))
  "Returns full string definition for message of type '<ask_BMI-response>"
  (cl:format cl:nil "float32 BMI~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ask_BMI-response)))
  "Returns full string definition for message of type 'ask_BMI-response"
  (cl:format cl:nil "float32 BMI~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ask_BMI-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ask_BMI-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ask_BMI-response
    (cl:cons ':BMI (BMI msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ask_BMI)))
  'ask_BMI-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ask_BMI)))
  'ask_BMI-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ask_BMI)))
  "Returns string type for a service object of type '<ask_BMI>"
  "beginner_tutorials/ask_BMI")