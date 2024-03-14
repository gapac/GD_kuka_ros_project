#!/usr/bin/env python

import rospy
# vkljucitev tipa Int64 iz std_msgs
from std_msgs.msg import Int64

if __name__ == '__main__':
    # node inicializaija
    # Options: DEBUG, INFO, WARN, ERROR, FATAL
    rospy.init_node("debug_test", anonymous=True,log_level=rospy.WARN)
    

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

    
        rospy.logdebug("Debug: Cnt je " + str(cnt))
        if cnt % 2:
            rospy.loginfo("Info: Cnt je " + str(cnt))
        if cnt == 5:
            rospy.logwarn("Warning: Smo na polovici!")
        if cnt == 9:
            rospy.logerr("Error: Cnt je 9!" )
        

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
            rospy.logfatal("Fatal: Cnt je 10. Reset cnt!")
        # zakasnitev, da se zagotovi ustrezno frekvenco izvajanja
        rate.sleep()
