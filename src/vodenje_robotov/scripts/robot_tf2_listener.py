#!/usr/bin/env python  
import rospy
import tf2_ros
from geometry_msgs.msg import Pose


if __name__ == '__main__':
    rospy.init_node('robot_tf2_listener')

    # definicija listener
    tfBuffer = tf2_ros.Buffer() # buffer 10 sekund
    listener = tf2_ros.TransformListener(tfBuffer)

    # definicija publisherja za rqt_plot
    pub = rospy.Publisher('/dron_pose',Pose,queue_size=10)
    p_dron = Pose()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            # preberi transformacijo
            trans = tfBuffer.lookup_transform("dron_1", 'world', rospy.Time(0))
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue

        # izpisi vrednost
        # print(trans.transform.translation)
        p_dron.position.x = trans.transform.translation.x
        p_dron.position.y = trans.transform.translation.y
        p_dron.position.z = trans.transform.translation.z
        pub.publish(p_dron)
       
        rate.sleep()