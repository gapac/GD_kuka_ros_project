#!/usr/bin/env python

import rospy
# vkljucitev tipa Int64 iz std_msgs
from std_msgs.msg import Int64

if __name__ == '__main__':
    # node inicializaija
    rospy.init_node("number_publisher", anonymous=True)
    rospy.loginfo('This node started.')
    # deklaracija publisherja
    pub = rospy.Publisher("/number", Int64, queue_size=10)
    # nastavitev frekvence izvajanja - 2 Hz
    rate = rospy.Rate(2)

    print('Sending number.')
    list = [1,2,3,4,5,6,7,8,9,10]
    cnt = 0
    
    # dokler se node ne ugasne, izvajaj sledeco kodo
    while not rospy.is_shutdown():
        # deklaracija sporocila
        msg = Int64()
        # definicija vrednosti sporocila
        msg.data = list[cnt]
        # posiljanje sporocila
        pub.publish(msg)
        # povecaj podatek
        cnt += 1
        if cnt == 10:
            cnt = 0
        # zakasnitev, da se zagotovi ustrezno frekvenco izvajanja
        rate.sleep()
