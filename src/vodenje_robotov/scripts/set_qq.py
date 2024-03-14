#!/usr/bin/env python

import rospy
import math
# vkljucitev tipa Int64 iz std_msgs
from std_msgs.msg import Float32
from sensor_msgs.msg import JointState


RATE = 10   # frekvenca posiljanja podatkov
FREQ = 0.5    # frekvenca sinusa

if __name__ == '__main__':
    # node inicializaija
    rospy.init_node("set_qq", anonymous=True)
    rospy.loginfo('This node started.')
    # deklaracija publisherja
    pub = rospy.Publisher("/joint_states", JointState, queue_size=10)
    # nastavitev frekvence izvajanja - 10 Hz
    rate = rospy.Rate(RATE)
    step = 0

    print('Sending qq.')

    # deklaracija sporocila
    qq = JointState()
    qq.name = ["axis_joint_1", "axis_joint_2", "axis_joint_3", "axis_joint_4", "axis_joint_5", "axis_joint_6"]
    
    # dokler se node ne ugasne, izvajaj sledeco kodo
    while not rospy.is_shutdown():
        
        # definicija vrednosti sporocila
        range = 30*math.pi/180# radianov
        qq.position = [0,0,range*math.sin(2*math.pi*FREQ*step/RATE),0,0,0]
        qq.header.stamp = rospy.get_rostime()
        # posiljanje sporocila
        pub.publish(qq)
        # povecaj stevec
        step = step + 1 
        # zakasnitev, da se zagotovi ustrezno frekvenco izvajanja
        rate.sleep()
