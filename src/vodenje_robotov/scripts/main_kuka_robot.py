#!/usr/bin/env python
from mobile_robot_control import MobileRobotControl  # Assuming the class name is MobileRobotControl
from geometry_msgs.msg import Twist, Vector3

import time

platform = MobileRobotControl()  # Create an instance of the class
platform._check_odom_ready()  # Call the method

import numpy as np
import rospy
import os

cmd = rospy.Publisher("/cmd_vel", Twist, queue_size=1)


os.environ["ROS_MASTER_URI"] = "http://192.168.65.59:11311"
os.environ["ROS_IP"] = "192.168.65.176"
os.environ["ROS_HOST"] = "192.168.65.176"

#get scan data
platform._check_laser_ready()

last_idx_dist = 0
while not rospy.is_shutdown():
    LidarRange = np.array(platform.get_laser_full())
    # print(LidarRange)

    LidarRange[LidarRange < 0.05] = np.inf
    
    
    #get index of closest point
    closest_idx = np.argmin(LidarRange)
    ClosestObject = LidarRange[closest_idx]
    

    print("IDX: ", closest_idx)

    print(ClosestObject)

    #P-regulator for distance to object
    idx_dist = closest_idx - 270
    if ClosestObject < 2.5:
        Kp = 0.2
        Kpr = 0.05
        Kdr = 0.0

        regVel_x = -Kp * (ClosestObject - 0.5) #0.5 is the desired distance from the object
        regVel_r = Kpr * idx_dist + Kdr * (idx_dist - last_idx_dist)
        #regVel_fi = Kp * ()-
        #platform.move_straight_turn() # Call the method
        print(regVel_x)
    else:
        regVel_x = 0
        #regVel_fi = 0
        #platform.move_straight_turn() # Call the method

    last_idx_dist = idx_dist
    regVel_x = np.clip(regVel_x, -0.5, 0.5)
    regVel_r = np.clip(regVel_r, -0.5, 0.5)

    # msg = Twist()
    # msg.linear.x = regVel_x
    # cmd.publish(msg)
    platform.move_straight(regVel_x, regVel_r) # Call the method

    #wit for 5sec
    time.sleep(0.100)

    #stop the platform
    # platform.stop_robot()
