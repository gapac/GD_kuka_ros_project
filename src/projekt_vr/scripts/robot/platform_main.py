from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]

from .laser import LaserScanner
from .mobile import MobileController
from .pid import PIDController

import numpy as np
import rospy


__all__ = ("Platform",)


class Platform:
    """
    The main class for kuka platform.
    """
    LASER_WAIT_SLEEP = 1

    def __init__(
        self,
        node: str,
        mobile: MobileController,
        laser: LaserScanner,
    ) -> None:
        self.mobile = mobile
        self.laser = laser

        self.pid_x = PIDController(0.2, 0.0, 0.0)
        self.pid_rz = PIDController(0.001, 0.0, 0.0)
        self.running = True
        self.node = node

        rospy.on_shutdown(self._on_shutdown)
    
    def init_node(self):
        rospy.init_node(self.node, anonymous=True)

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
            distance_mask = distances < max_distance
            angles = angles[distance_mask]
            distances = distances[distance_mask]

            # Get closest distance and its angle
            idx = distances.argmin()  # Alternative is to use distance gradients over angle
            distance = distances[idx]
            angle = angles[idx]

            # Safety clipping
            x_speed = np.clip(self.pid_x.step(target_x - distance), -0.2, 0.2)
            rot_speed = np.clip(self.pid_rz.step(angle), -15, 15)

            # Control
            self.mobile.control_speeds(x_speed, 0, 0, rot_speed)
            rospy.sleep(0.100)

        self.mobile.stop_movement()
