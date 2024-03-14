;; Auto-generated. Do not edit!


(when (boundp 'slam_toolbox_msgs::Reset)
  (if (not (find-package "SLAM_TOOLBOX_MSGS"))
    (make-package "SLAM_TOOLBOX_MSGS"))
  (shadow 'Reset (find-package "SLAM_TOOLBOX_MSGS")))
(unless (find-package "SLAM_TOOLBOX_MSGS::RESET")
  (make-package "SLAM_TOOLBOX_MSGS::RESET"))
(unless (find-package "SLAM_TOOLBOX_MSGS::RESETREQUEST")
  (make-package "SLAM_TOOLBOX_MSGS::RESETREQUEST"))
(unless (find-package "SLAM_TOOLBOX_MSGS::RESETRESPONSE")
  (make-package "SLAM_TOOLBOX_MSGS::RESETRESPONSE"))

(in-package "ROS")





(defclass slam_toolbox_msgs::ResetRequest
  :super ros::object
  :slots (_pause_new_measurements ))

(defmethod slam_toolbox_msgs::ResetRequest
  (:init
   (&key
    ((:pause_new_measurements __pause_new_measurements) nil)
    )
   (send-super :init)
   (setq _pause_new_measurements __pause_new_measurements)
   self)
  (:pause_new_measurements
   (&optional (__pause_new_measurements :null))
   (if (not (eq __pause_new_measurements :null)) (setq _pause_new_measurements __pause_new_measurements)) _pause_new_measurements)
  (:serialization-length
   ()
   (+
    ;; bool _pause_new_measurements
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _pause_new_measurements
       (if _pause_new_measurements (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _pause_new_measurements
     (setq _pause_new_measurements (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(intern "*RESULT_SUCCESS*" (find-package "SLAM_TOOLBOX_MSGS::RESETRESPONSE"))
(shadow '*RESULT_SUCCESS* (find-package "SLAM_TOOLBOX_MSGS::RESETRESPONSE"))
(defconstant slam_toolbox_msgs::ResetResponse::*RESULT_SUCCESS* 0)

(defun slam_toolbox_msgs::ResetResponse-to-symbol (const)
  (cond
        ((= const 0) 'slam_toolbox_msgs::ResetResponse::*RESULT_SUCCESS*)
        (t nil)))

(defclass slam_toolbox_msgs::ResetResponse
  :super ros::object
  :slots (_result ))

(defmethod slam_toolbox_msgs::ResetResponse
  (:init
   (&key
    ((:result __result) 0)
    )
   (send-super :init)
   (setq _result (round __result))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:serialization-length
   ()
   (+
    ;; uint8 _result
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _result
       (write-byte _result s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _result
     (setq _result (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(defclass slam_toolbox_msgs::Reset
  :super ros::object
  :slots ())

(setf (get slam_toolbox_msgs::Reset :md5sum-) "d183d6d1f6b03b1483ab508f22fac253")
(setf (get slam_toolbox_msgs::Reset :datatype-) "slam_toolbox_msgs/Reset")
(setf (get slam_toolbox_msgs::Reset :request) slam_toolbox_msgs::ResetRequest)
(setf (get slam_toolbox_msgs::Reset :response) slam_toolbox_msgs::ResetResponse)

(defmethod slam_toolbox_msgs::ResetRequest
  (:response () (instance slam_toolbox_msgs::ResetResponse :init)))

(setf (get slam_toolbox_msgs::ResetRequest :md5sum-) "d183d6d1f6b03b1483ab508f22fac253")
(setf (get slam_toolbox_msgs::ResetRequest :datatype-) "slam_toolbox_msgs/ResetRequest")
(setf (get slam_toolbox_msgs::ResetRequest :definition-)
      "# Set this to 'true' to pause new measurements immediately after reset.
# Note: This is a set behaviour and not a toggle behaviour, contrary to Pause.srv service.
bool pause_new_measurements
---
# Result code defintions
uint8 RESULT_SUCCESS=0

uint8 result

")

(setf (get slam_toolbox_msgs::ResetResponse :md5sum-) "d183d6d1f6b03b1483ab508f22fac253")
(setf (get slam_toolbox_msgs::ResetResponse :datatype-) "slam_toolbox_msgs/ResetResponse")
(setf (get slam_toolbox_msgs::ResetResponse :definition-)
      "# Set this to 'true' to pause new measurements immediately after reset.
# Note: This is a set behaviour and not a toggle behaviour, contrary to Pause.srv service.
bool pause_new_measurements
---
# Result code defintions
uint8 RESULT_SUCCESS=0

uint8 result

")



(provide :slam_toolbox_msgs/Reset "d183d6d1f6b03b1483ab508f22fac253")


