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

    def _on_shutdown(self):
        self.stop_tracking()

    def stop_tracking(self):
        self.running = False

    def track_closest_object(
        self,
        min_distance: float = 0.050,
        max_distance: float = 2.0,
        target_x: float = 0.5
    ):
        # TODO: test if it works
        self.pid_x.zero()
        self.pid_rz.zero()
        while self.running:
            rospy.sleep(0.100)
            distances = self.laser.get_distances()
            if distances is None:
                rospy.logerr("Could not laser data, stopping tracking.")
                break

            angles = self.laser.get_indices_angles()
            dist_angle = np.array(zip(distances, angles))

            # The error distance and error angle
            distance, angle = dist_angle[(distances < max_distance) & (distances > min_distance)]
            
            x_speed = np.clip(self.pid_x.step(target_x - distance), -0.2, 0.2)
            rot_speed = np.clip(self.pid_rz.step(angle), -15, 15)
            self.mobile.control_speeds(x_speed, 0, 0, rot_speed)

        self.mobile.stop_movement()
