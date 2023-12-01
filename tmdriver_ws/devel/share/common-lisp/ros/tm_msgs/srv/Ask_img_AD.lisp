; Auto-generated. Do not edit!


(cl:in-package tm_msgs-srv)


;//! \htmlinclude Ask_img_AD-request.msg.html

(cl:defclass <Ask_img_AD-request> (roslisp-msg-protocol:ros-message)
  ((file_path
    :reader file_path
    :initarg :file_path
    :type cl:string
    :initform ""))
)

(cl:defclass Ask_img_AD-request (<Ask_img_AD-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ask_img_AD-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ask_img_AD-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<Ask_img_AD-request> is deprecated: use tm_msgs-srv:Ask_img_AD-request instead.")))

(cl:ensure-generic-function 'file_path-val :lambda-list '(m))
(cl:defmethod file_path-val ((m <Ask_img_AD-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:file_path-val is deprecated.  Use tm_msgs-srv:file_path instead.")
  (file_path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ask_img_AD-request>) ostream)
  "Serializes a message object of type '<Ask_img_AD-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'file_path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'file_path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ask_img_AD-request>) istream)
  "Deserializes a message object of type '<Ask_img_AD-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'file_path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'file_path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ask_img_AD-request>)))
  "Returns string type for a service object of type '<Ask_img_AD-request>"
  "tm_msgs/Ask_img_ADRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img_AD-request)))
  "Returns string type for a service object of type 'Ask_img_AD-request"
  "tm_msgs/Ask_img_ADRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ask_img_AD-request>)))
  "Returns md5sum for a message object of type '<Ask_img_AD-request>"
  "718c3a88dd0f5e8414a94bc17ba46265")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ask_img_AD-request)))
  "Returns md5sum for a message object of type 'Ask_img_AD-request"
  "718c3a88dd0f5e8414a94bc17ba46265")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ask_img_AD-request>)))
  "Returns full string definition for message of type '<Ask_img_AD-request>"
  (cl:format cl:nil "string file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ask_img_AD-request)))
  "Returns full string definition for message of type 'Ask_img_AD-request"
  (cl:format cl:nil "string file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ask_img_AD-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'file_path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ask_img_AD-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Ask_img_AD-request
    (cl:cons ':file_path (file_path msg))
))
;//! \htmlinclude Ask_img_AD-response.msg.html

(cl:defclass <Ask_img_AD-response> (roslisp-msg-protocol:ros-message)
  ((anomaly_score
    :reader anomaly_score
    :initarg :anomaly_score
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Ask_img_AD-response (<Ask_img_AD-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ask_img_AD-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ask_img_AD-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tm_msgs-srv:<Ask_img_AD-response> is deprecated: use tm_msgs-srv:Ask_img_AD-response instead.")))

(cl:ensure-generic-function 'anomaly_score-val :lambda-list '(m))
(cl:defmethod anomaly_score-val ((m <Ask_img_AD-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tm_msgs-srv:anomaly_score-val is deprecated.  Use tm_msgs-srv:anomaly_score instead.")
  (anomaly_score m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ask_img_AD-response>) ostream)
  "Serializes a message object of type '<Ask_img_AD-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'anomaly_score))))
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
   (cl:slot-value msg 'anomaly_score))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ask_img_AD-response>) istream)
  "Deserializes a message object of type '<Ask_img_AD-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'anomaly_score) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'anomaly_score)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ask_img_AD-response>)))
  "Returns string type for a service object of type '<Ask_img_AD-response>"
  "tm_msgs/Ask_img_ADResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img_AD-response)))
  "Returns string type for a service object of type 'Ask_img_AD-response"
  "tm_msgs/Ask_img_ADResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ask_img_AD-response>)))
  "Returns md5sum for a message object of type '<Ask_img_AD-response>"
  "718c3a88dd0f5e8414a94bc17ba46265")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ask_img_AD-response)))
  "Returns md5sum for a message object of type 'Ask_img_AD-response"
  "718c3a88dd0f5e8414a94bc17ba46265")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ask_img_AD-response>)))
  "Returns full string definition for message of type '<Ask_img_AD-response>"
  (cl:format cl:nil "float64[] anomaly_score ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ask_img_AD-response)))
  "Returns full string definition for message of type 'Ask_img_AD-response"
  (cl:format cl:nil "float64[] anomaly_score ~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ask_img_AD-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'anomaly_score) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ask_img_AD-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Ask_img_AD-response
    (cl:cons ':anomaly_score (anomaly_score msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Ask_img_AD)))
  'Ask_img_AD-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Ask_img_AD)))
  'Ask_img_AD-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ask_img_AD)))
  "Returns string type for a service object of type '<Ask_img_AD>"
  "tm_msgs/Ask_img_AD")