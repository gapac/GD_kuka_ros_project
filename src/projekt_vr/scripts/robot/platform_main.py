from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]

from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Joy

from .laser import LaserScanner
from .mobile import MobileController
from .pid import PIDController
from .arm import ArmController

import numpy as np
import rospy
import matplotlib.pyplot as plt


__all__ = ("Platform",)


class Platform:
    """
    The main class for kuka platform.
    """
    LASER_WAIT_SLEEP = 1

    def __init__(
        self,
        mobile: MobileController,
        laser: LaserScanner,
        arm: ArmController
    ) -> None:
        self.mobile = mobile
        self.laser = laser
        self.arm = arm
        self.xyz_data = None

        self.pid_x = PIDController(0.2, 0.0, 0.0)
        self.pid_rz = PIDController(0.01, 0.0, 0.0)
        self.running = True

        rospy.on_shutdown(self._on_shutdown)

    def wait_ready(self):
        while self.running:
            data = self.laser.get_distances()
            if data is not None:
                rospy.loginfo("LASER READY")
                break

            rospy.loginfo("LASER NOT READY, retrying")
            rospy.sleep(Platform.LASER_WAIT_SLEEP)

    def _on_shutdown(self):
        self.stop()
        self.mobile.stop_movement()

    def stop(self):
        self.running = False

    def track_closest_object(
        self,
        max_distance: float = 2.0,
        target_x: float = 0.5
    ):
        # TODO: test if it works
        self.pid_x.zero()
        self.pid_rz.zero()
        plt.ion()
        while self.running:
            distances = self.laser.get_distances()
            if distances is None:
                rospy.logerr("Could not laser data, stopping tracking.")
                break

            angles: np.ndarray = np.array(self.laser.get_indices_angles())
            distances: np.ndarray = np.array(distances)

            # Only consider angles that are -90 + 90 degrees relative to the X (forward) axis
            angle_mask =  (angles > -90) & (angles < 90)

            angles = angles[angle_mask]
            distances = distances[angle_mask]

            # Filter out points further than max_distance
            #distances[np.isinf(distances)] = 20
            distance_mask = distances < max_distance
            angles = angles[distance_mask]
            distances = distances[distance_mask]
            #gradients = np.gradient(distances, angles)
            # Filter out points that are too close to each other
            if len(distances):
                # Get closest distance and its angle

                idx = distances.argmin()
                distance = distances[idx]
                angle = angles[idx]

                # Safety clipping
                dist_error = abs(distance - target_x)
                if dist_error < 0.1:
                    self.mobile.control_speeds(0, 0, 0, 0)
                    self.give_chocolate()
                    rospy.sleep(5)

                x_speed = -np.clip(self.pid_x.step(distance - target_x), -0.2, 0.2)
                rot_speed = np.clip(self.pid_rz.step(angle), -0.5, 0.5)

                # Control
                self.mobile.control_speeds(x_speed, 0, 0, rot_speed)

            rospy.sleep(0.200)

        self.mobile.stop_movement()


    def give_chocolate(self):
        arm = self.arm
        # GRIP OFF
        arm.open_gripper()
        arm.move_arm(0.1)
        arm.move_arm(0.1, joint="arm_joint_2")
        arm.move_arm(0.1, joint="arm_joint_3")
        arm.move_arm(0.1, joint="arm_joint_4")
        arm.move_arm(0.1, joint="arm_joint_5")
        arm.move_arm(3.05)
        rospy.sleep(2)
        arm.move_arm(-2.85, joint="arm_joint_3")
        # # GRIP ON
        arm.close_gripper()
        arm.move_arm(-1.0, joint="arm_joint_3")
        arm.move_arm(1.5, joint="arm_joint_2")
