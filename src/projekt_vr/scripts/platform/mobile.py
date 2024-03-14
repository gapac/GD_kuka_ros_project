from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]
from geometry_msgs.msg import Twist, Vector3

import rospy


class MobileController:
    """
    Mobile platform controller.

    Parameters
    --------------
    vel_topic: str
        The name of velocity control topic.
    retry_interval: float
        Interval in seconds at which to wait
        for connections when publishing reliably.
    """
    def __init__(
        self,
        vel_topic: str = "/cmd_vel",
        retry_interval: float = 1.0,
    ) -> None:
        # Command data
        self.speed_msg = Twist()

        self.vel_pub = rospy.Publisher(vel_topic, Twist, queue_size=1)
        self.retry_interval = retry_interval
        rospy.on_shutdown(self._on_shutdown)  # Stop the robot on rospy shutdown

    def control_speeds(self, x: float, y: float, z: float, rot_z: float):
        """
        Moves the platform with given directional speeds.

        This should be called on regular intervals as publish is unreliable.
        """
        self._set_speeds(x, y, z, rot_z)
        self._publish_fast()

    def _set_speeds(self, x: float, y: float, z: float, rot_z: float):
        self.speed_msg.linear = Vector3(x, y, z)
        self.speed_msg.angular.z = rot_z

    def stop_movement(self):
        self._set_speeds(0, 0, 0, 0)
        self._publish_reliable()

    def _publish_fast(self):
        """
        Fast publish, without checking if any connections are available.
        """
        rospy.logdebug("Connection unreliably published.")
        self.vel_pub.publish(self.speed_msg)

    def _publish_reliable(self):
        """
        Fast publish, with waiting connections for at least one connection.
        """
        while not rospy.is_shutdown():
            n_conn = self.vel_pub.get_num_connections()
            if n_conn > 0:
                self.vel_pub.publish(self.speed_msg)
                rospy.logdebug("Connection reliably published.")
            else:
                rospy.sleep(self.retry_interval)

    def _on_shutdown(self):
        self.stop_movement()
