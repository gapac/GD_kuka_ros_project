#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan
import time


class RobotControl():

    def __init__(self):
        rospy.init_node('robot_control_node', anonymous=True)

        cmd_vel_topic='/cmd_vel'
        self._check_laser_ready()

        # start the publisher
        self.vel_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=1)
        self.cmd = Twist()        

        self.odom_subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.sick_laser_subscriber = rospy.Subscriber('/sick_nanoscan3/scan', LaserScan, self.sick_laser_callback)
        
        self.ctrl_c = False
        self.rate = rospy.Rate(1)
        rospy.on_shutdown(self.shutdownhook)

    
    def _check_odom_ready(self):
        self.odom_msg = None
        rospy.loginfo("Checking Summit Laser...")
        while self.odom_msg is None and not rospy.is_shutdown():
            try:
                self.odom_msg = rospy.wait_for_message("/odom", Odometry, timeout=1.0)
                rospy.logdebug("Current /odom READY=>" + str(self.odom_msg))

            except:
                rospy.logerr("Current /odom not ready yet, retrying for getting scan")
        rospy.loginfo("Checking /odom...DONE")
        return self.odom_msg

    def _check_laser_ready(self):
        self.laser_msg = None
        rospy.loginfo("Checking Sick NanoScan3 laser...")
        while self.laser_msg is None and not rospy.is_shutdown():
            try:
                self.laser_msg = rospy.wait_for_message("/sick_nanoscan3/scan", LaserScan, timeout=1.0)
                rospy.logdebug("Current /sick_nanoscan3/scan READY=>" + str(self.laser_msg))

            except:
                rospy.logerr("Current /sick_nanoscan3/scan not ready yet, retrying for getting scan")
        rospy.loginfo("Checking SICK Nanoscan3...DONE")
        return self.laser_msg

    def publish_once_in_cmd_vel(self):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems, this is no big deal, but in systems that publish only
        once, it IS very important.
        """
        while not self.ctrl_c:
            connections = self.vel_publisher.get_num_connections()
            if connections > 0:
                self.vel_publisher.publish(self.cmd)
                #rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()

		if self.ctrl_c:
			self.vel_publisher.publish(self.cmd)



    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
		self.stop_robot()

    def laser_callback(self, msg):
        self.laser_msg = msg

    '''def odom_callback(self, msg):
        self.odom_msg = msg'''

    '''def get_laser(self, pos):
        time.sleep(1)
        return self.laser_msg.ranges[pos]'''

    def get_laser_full(self):
        time.sleep(1)
        return self.laser_msg.ranges

    def stop_robot(self):
        #rospy.loginfo("shutdown time! Stop the robot")
        self.cmd.linear = Vector3(0.0, 0.0, 0.0)
        self.cmd.angular = Vector3(0.0, 0.0, 0.0)
        self.publish_once_in_cmd_vel()

    def move_straight(self):

        # Initilize velocities
        self.cmd.linear.x = 0.05
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0
        self.cmd.angular.z = 0

        # Publish the velocity
        self.publish_once_in_cmd_vel()

    def move_straight_time(self, motion, speed, time):

        # Initilize velocities
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0
        self.cmd.angular.z = 0

        if motion == "forward":
            self.cmd.linear.x = speed
        elif motion == "backward":
            self.cmd.linear.x = - speed

        i = 0
        # loop to publish the velocity estimate, current_distance = velocity * (t1 - t0)
        while (i <= time):

            # Publish the velocity
            self.vel_publisher.publish(self.cmd)
            i += 1
            self.rate.sleep()

        # set velocity to zero to stop the robot
        self.stop_robot()

        s = "Moved robot " + motion + " for " + str(time) + " seconds"
        return s


    def turn(self, clockwise, speed, time):

        # Initilize velocities
        self.cmd.linear.x = 0
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.cmd.angular.x = 0
        self.cmd.angular.y = 0

        if clockwise == "clockwise":
            self.cmd.angular.z = -speed
        else:
            self.cmd.angular.z = speed

        i = 0
        # loop to publish the velocity estimate, current_distance = velocity * (t1 - t0)
        while (i <= time):

            # Publish the velocity
            self.vel_publisher.publish(self.cmd)
            i += 1
            self.rate.sleep()

        # set velocity to zero to stop the robot
        self.stop_robot()

        s = "Turned robot " + clockwise + " for " + str(time) + " seconds"
        return s


if __name__ == '__main__':
    
    robotcontrol_object = RobotControl()
    try:
        robotcontrol_object.move_straight()

    except rospy.ROSInterruptException:
        pass

