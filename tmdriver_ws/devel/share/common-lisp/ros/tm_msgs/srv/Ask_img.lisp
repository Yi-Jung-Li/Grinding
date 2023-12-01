; Auto-generated. Do not edit!


(cl:in-package tm_msgs-srv)


;//! \htmlinclude Ask_img-request.msg.html

(cl:defclass <Ask_img-request> (roslisp-msg-protocol:ros-message)
  ((file_name
    :reader file_name
    :initarg :file_name
    :type cl:string
    :initform ""))
)

(cl:defclass Ask_img-request (<Ask_img-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ask_img-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ask_img-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<Ask_img-request> is deprecated: use tm_msgs-srv:Ask_img-request instead.")))

(cl:ensure-generic-function 'file_name-val :lambda-list '(m))
(cl:defmethod file_name-val ((m <Ask_img-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:file_name-val is deprecated.  Use tm_msgs-srv:file_name instead.")
  (file_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ask_img-request>) ostream)
  "Serializes a message object of type '<Ask_img-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'file_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'file_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ask_img-request>) istream)
  "Deserializes a message object of type '<Ask_img-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'file_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'file_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ask_img-request>)))
  "Returns string type for a service object of type '<Ask_img-request>"
  "tm_msgs/Ask_imgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img-request)))
  "Returns string type for a service object of type 'Ask_img-request"
  "tm_msgs/Ask_imgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ask_img-request>)))
  "Returns md5sum for a message object of type '<Ask_img-request>"
  "dc18f33ad8fd47637626ae0ea2c4eb17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ask_img-request)))
  "Returns md5sum for a message object of type 'Ask_img-request"
  "dc18f33ad8fd47637626ae0ea2c4eb17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ask_img-request>)))
  "Returns full string definition for message of type '<Ask_img-request>"
  (cl:format cl:nil "string file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ask_img-request)))
  "Returns full string definition for message of type 'Ask_img-request"
  (cl:format cl:nil "string file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ask_img-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'file_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ask_img-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Ask_img-request
    (cl:cons ':file_name (file_name msg))
))
;//! \htmlinclude Ask_img-response.msg.html

(cl:defclass <Ask_img-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil)
   (error
    :reader error
    :initarg :error
    :type cl:string
    :initform ""))
)

(cl:defclass Ask_img-response (<Ask_img-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ask_img-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ask_img-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<Ask_img-response> is deprecated: use tm_msgs-srv:Ask_img-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <Ask_img-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:ok-val is deprecated.  Use tm_msgs-srv:ok instead.")
  (ok m))

(cl:ensure-generic-function 'error-val :lambda-list '(m))
(cl:defmethod error-val ((m <Ask_img-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:error-val is deprecated.  Use tm_msgs-srv:error instead.")
  (error m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ask_img-response>) ostream)
  "Serializes a message object of type '<Ask_img-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'error))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'error))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ask_img-response>) istream)
  "Deserializes a message object of type '<Ask_img-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'error) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'error) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ask_img-response>)))
  "Returns string type for a service object of type '<Ask_img-response>"
  "tm_msgs/Ask_imgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img-response)))
  "Returns string type for a service object of type 'Ask_img-response"
  "tm_msgs/Ask_imgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ask_img-response>)))
  "Returns md5sum for a message object of type '<Ask_img-response>"
  "dc18f33ad8fd47637626ae0ea2c4eb17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ask_img-response)))
  "Returns md5sum for a message object of type 'Ask_img-response"
  "dc18f33ad8fd47637626ae0ea2c4eb17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ask_img-response>)))
  "Returns full string definition for message of type '<Ask_img-response>"
  (cl:format cl:nil "bool ok~%string error~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ask_img-response)))
  "Returns full string definition for message of type 'Ask_img-response"
  (cl:format cl:nil "bool ok~%string error~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ask_img-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'error))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ask_img-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Ask_img-response
    (cl:cons ':ok (ok msg))
    (cl:cons ':error (error msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Ask_img)))
  'Ask_img-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Ask_img)))
  'Ask_img-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img)))
  "Returns string type for a service object of type '<Ask_img>"
  "tm_msgs/Ask_img")