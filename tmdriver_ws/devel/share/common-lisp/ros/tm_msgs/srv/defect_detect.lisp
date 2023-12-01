; Auto-generated. Do not edit!


(cl:in-package tm_msgs-srv)


;//! \htmlinclude defect_detect-request.msg.html

(cl:defclass <defect_detect-request> (roslisp-msg-protocol:ros-message)
  ((function
    :reader function
    :initarg :function
    :type cl:string
    :initform ""))
)

(cl:defclass defect_detect-request (<defect_detect-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <defect_detect-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'defect_detect-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<defect_detect-request> is deprecated: use tm_msgs-srv:defect_detect-request instead.")))

(cl:ensure-generic-function 'function-val :lambda-list '(m))
(cl:defmethod function-val ((m <defect_detect-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:function-val is deprecated.  Use tm_msgs-srv:function instead.")
  (function m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <defect_detect-request>) ostream)
  "Serializes a message object of type '<defect_detect-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'function))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'function))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <defect_detect-request>) istream)
  "Deserializes a message object of type '<defect_detect-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'function) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'function) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<defect_detect-request>)))
  "Returns string type for a service object of type '<defect_detect-request>"
  "tm_msgs/defect_detectRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'defect_detect-request)))
  "Returns string type for a service object of type 'defect_detect-request"
  "tm_msgs/defect_detectRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<defect_detect-request>)))
  "Returns md5sum for a message object of type '<defect_detect-request>"
  "bcee4f588ea52289bf77bc6d6629f851")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'defect_detect-request)))
  "Returns md5sum for a message object of type 'defect_detect-request"
  "bcee4f588ea52289bf77bc6d6629f851")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<defect_detect-request>)))
  "Returns full string definition for message of type '<defect_detect-request>"
  (cl:format cl:nil "string function ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'defect_detect-request)))
  "Returns full string definition for message of type 'defect_detect-request"
  (cl:format cl:nil "string function ~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <defect_detect-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'function))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <defect_detect-request>))
  "Converts a ROS message object to a list"
  (cl:list 'defect_detect-request
    (cl:cons ':function (function msg))
))
;//! \htmlinclude defect_detect-response.msg.html

(cl:defclass <defect_detect-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass defect_detect-response (<defect_detect-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <defect_detect-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'defect_detect-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<defect_detect-response> is deprecated: use tm_msgs-srv:defect_detect-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <defect_detect-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:ok-val is deprecated.  Use tm_msgs-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <defect_detect-response>) ostream)
  "Serializes a message object of type '<defect_detect-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <defect_detect-response>) istream)
  "Deserializes a message object of type '<defect_detect-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<defect_detect-response>)))
  "Returns string type for a service object of type '<defect_detect-response>"
  "tm_msgs/defect_detectResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'defect_detect-response)))
  "Returns string type for a service object of type 'defect_detect-response"
  "tm_msgs/defect_detectResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<defect_detect-response>)))
  "Returns md5sum for a message object of type '<defect_detect-response>"
  "bcee4f588ea52289bf77bc6d6629f851")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'defect_detect-response)))
  "Returns md5sum for a message object of type 'defect_detect-response"
  "bcee4f588ea52289bf77bc6d6629f851")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<defect_detect-response>)))
  "Returns full string definition for message of type '<defect_detect-response>"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'defect_detect-response)))
  "Returns full string definition for message of type 'defect_detect-response"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <defect_detect-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <defect_detect-response>))
  "Converts a ROS message object to a list"
  (cl:list 'defect_detect-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'defect_detect)))
  'defect_detect-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'defect_detect)))
  'defect_detect-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'defect_detect)))
  "Returns string type for a service object of type '<defect_detect>"
  "tm_msgs/defect_detect")