from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]

from .laser import LaserScanner
from .mobile import MobileController
from .pid import PIDController

import rospy


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

        rospy.init_node(node, anonymous=True)
        self.pid_x = PIDController(0.2, 0.0, 0.0)
        self.pid_rz = PIDController(0.5, 0.0, 0.0)

    def track_closest_object(self, min_distance: float = 2.0):
        # TODO: ...
        ...
