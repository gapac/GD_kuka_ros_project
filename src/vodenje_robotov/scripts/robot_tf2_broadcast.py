#!/usr/bin/env python  
import rospy
import tf
import tf2_ros
import geometry_msgs.msg
import math

if __name__ == '__main__':
    rospy.init_node('robot_tf2_broadcaster')
    
    # definicija broadcasterja
    br = tf2_ros.TransformBroadcaster()
    # deklaracija transformacije
    trans = geometry_msgs.msg.TransformStamped()

    # definicija parent/child
    trans.header.frame_id = "robot_2"
    trans.child_frame_id = "dron_1"

    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        
        x = rospy.Time.now().to_sec() * math.pi

        # trenutni cas
        trans.header.stamp = rospy.Time.now()
        # pozicija
        trans.transform.translation.x = 0.5 * math.sin(x/2)
        trans.transform.translation.y = 0.5 * math.cos(x/2)
        trans.transform.translation.z = 0
        
        # orientacija
        # quaternion_from_euler(roll,pitch,yaw)
        # RPY - ZYX
        my_quat = tf.transformations.quaternion_from_euler(0,0,0)
        #RPY = tf.transformations.euler_from_quaternion([x,y,z,w])
        trans.transform.rotation.x = my_quat[0]
        trans.transform.rotation.y = my_quat[1]
        trans.transform.rotation.z = my_quat[2]
        trans.transform.rotation.w = my_quat[3]

        # poslji transformacijo
        br.sendTransform(trans)

        rate.sleep()