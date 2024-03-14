; Auto-generated. Do not edit!


(cl:in-package slam_toolbox_msgs-srv)


;//! \htmlinclude Reset-request.msg.html

(cl:defclass <Reset-request> (roslisp-msg-protocol:ros-message)
  ((pause_new_measurements
    :reader pause_new_measurements
    :initarg :pause_new_measurements
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Reset-request (<Reset-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reset-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reset-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name slam_toolbox_msgs-srv:<Reset-request> is deprecated: use slam_toolbox_msgs-srv:Reset-request instead.")))

(cl:ensure-generic-function 'pause_new_measurements-val :lambda-list '(m))
(cl:defmethod pause_new_measurements-val ((m <Reset-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader slam_toolbox_msgs-srv:pause_new_measurements-val is deprecated.  Use slam_toolbox_msgs-srv:pause_new_measurements instead.")
  (pause_new_measurements m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reset-request>) ostream)
  "Serializes a message object of type '<Reset-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'pause_new_measurements) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reset-request>) istream)
  "Deserializes a message object of type '<Reset-request>"
    (cl:setf (cl:slot-value msg 'pause_new_measurements) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Reset-request>)))
  "Returns string type for a service object of type '<Reset-request>"
  "slam_toolbox_msgs/ResetRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reset-request)))
  "Returns string type for a service object of type 'Reset-request"
  "slam_toolbox_msgs/ResetRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Reset-request>)))
  "Returns md5sum for a message object of type '<Reset-request>"
  "d183d6d1f6b03b1483ab508f22fac253")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reset-request)))
  "Returns md5sum for a message object of type 'Reset-request"
  "d183d6d1f6b03b1483ab508f22fac253")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reset-request>)))
  "Returns full string definition for message of type '<Reset-request>"
  (cl:format cl:nil "# Set this to 'true' to pause new measurements immediately after reset.~%# Note: This is a set behaviour and not a toggle behaviour, contrary to Pause.srv service.~%bool pause_new_measurements~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reset-request)))
  "Returns full string definition for message of type 'Reset-request"
  (cl:format cl:nil "# Set this to 'true' to pause new measurements immediately after reset.~%# Note: This is a set behaviour and not a toggle behaviour, contrary to Pause.srv service.~%bool pause_new_measurements~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reset-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reset-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Reset-request
    (cl:cons ':pause_new_measurements (pause_new_measurements msg))
))
;//! \htmlinclude Reset-response.msg.html

(cl:defclass <Reset-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Reset-response (<Reset-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Reset-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Reset-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name slam_toolbox_msgs-srv:<Reset-response> is deprecated: use slam_toolbox_msgs-srv:Reset-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <Reset-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader slam_toolbox_msgs-srv:result-val is deprecated.  Use slam_toolbox_msgs-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<Reset-response>)))
    "Constants for message type '<Reset-response>"
  '((:RESULT_SUCCESS . 0))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'Reset-response)))
    "Constants for message type 'Reset-response"
  '((:RESULT_SUCCESS . 0))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Reset-response>) ostream)
  "Serializes a message object of type '<Reset-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Reset-response>) istream)
  "Deserializes a message object of type '<Reset-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Reset-response>)))
  "Returns string type for a service object of type '<Reset-response>"
  "slam_toolbox_msgs/ResetResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reset-response)))
  "Returns string type for a service object of type 'Reset-response"
  "slam_toolbox_msgs/ResetResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Reset-response>)))
  "Returns md5sum for a message object of type '<Reset-response>"
  "d183d6d1f6b03b1483ab508f22fac253")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Reset-response)))
  "Returns md5sum for a message object of type 'Reset-response"
  "d183d6d1f6b03b1483ab508f22fac253")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Reset-response>)))
  "Returns full string definition for message of type '<Reset-response>"
  (cl:format cl:nil "# Result code defintions~%uint8 RESULT_SUCCESS=0~%~%uint8 result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Reset-response)))
  "Returns full string definition for message of type 'Reset-response"
  (cl:format cl:nil "# Result code defintions~%uint8 RESULT_SUCCESS=0~%~%uint8 result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Reset-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Reset-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Reset-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Reset)))
  'Reset-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Reset)))
  'Reset-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Reset)))
  "Returns string type for a service object of type '<Reset>"
  "slam_toolbox_msgs/Reset")