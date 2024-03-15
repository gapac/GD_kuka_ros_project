from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]
from sensor_msgs.msg import LaserScan

import rospy


__all__ = ("LaserScanner",)


class LaserScanner:
    """
    Lidar controller.

    Parameters
    ---------------
    subscriber_topic: str
        The topic name of the laser.
    zero_angle_index: int
        The index (of ``get_distances``) corresponding to angle 0.
    """
    MAX_DATA_AGE_S = 1.0

    def __init__(
        self,
        subscriber_topic: str = "/scan",
        zero_angle_index: int = 270,
    ) -> None:
        self.subscriber = rospy.Subscriber(subscriber_topic, LaserScan, self._laser_scan_callback, queue_size=1)
        self.scan_data: list[float] = None
        self.last_scan_time = 0.0
        self.zero_angle_idx = zero_angle_index

    def _laser_scan_callback(self, msg: LaserScan):
        self.scan_data = msg.ranges
        self.last_scan_time = rospy.get_time()

    def get_distances(self):
        """
        Returns measured array of measured distances or None if the data is older than LaserScanner.MAX_DATA_AGE_S.
        """
        # Protection if laser stops working for some reason
        if (rospy.get_time() - self.last_scan_time) > LaserScanner.MAX_DATA_AGE_S:
            return None

        return self.scan_data

    def get_indices_angles(self):
        """
        Returns a list of angles corresponding to indices.
        """
        len_ = len(self.scan_data)
        slope = 360.0 / len_
        idx_offset = self.zero_angle_idx
        offset_angle = -slope * idx_offset  # 0 degrees = slope * idx_offset + offset_angle => offset_angle = 0 - slope * idx_offset
        return list(map(lambda idx: slope * idx + offset_angle, range(len_)))
