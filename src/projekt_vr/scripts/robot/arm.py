from __future__ import annotations  # Allows us to annotate list[float] instead of typing.List[float]
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy
from brics_actuator.msg import JointPositions, JointValue


import rospy
import numpy as np


__all__ = ("ArmController",)


class ArmController:
    """
    Arm controller.
    """
    def __init__(
        self,
        arm_topic: str = "/arm_1/arm_controller/position_command",
        gripper_topic: str = "/arm_1/gripper_controller/position_command",
    ) -> None:
        # Command data
        self.position_msg = JointPositions()

        self.arm_publisher = rospy.Publisher(arm_topic, JointPositions, queue_size=1, latch=True)
        self.gripper_publisher = rospy.Publisher(gripper_topic, JointPositions, queue_size=1, latch=True)

    def move_arm(self, angle: float, joint: str = "arm_joint_1"):
        """
        Move the arm to the specified angle in radians.
        """
        pos = JointValue()
        pos.unit = "rad"
        pos.value = angle
        pos.joint_uri = joint

        self.position_msg.positions = [pos]
        self.arm_publisher.publish(self.position_msg)
        rospy.sleep(1)

    def _set_gripper(self, value: float):
        pos = JointValue()
        pos.unit = "m"
        pos.value = value
        pos.joint_uri = "gripper_finger_joint_l"

        pos2 = JointValue()
        pos2.unit = "m"
        pos2.value = value
        pos2.joint_uri = "gripper_finger_joint_r"

        self.position_msg.positions = [pos, pos2]
        self.gripper_publisher.publish(self.position_msg)
        rospy.sleep(3)

    def open_gripper(self):
        """
        Open the gripper.
        """
        self._set_gripper(0.0115)

    def close_gripper(self):
        """
        Close the gripper.
        """
        self._set_gripper(0.0)
