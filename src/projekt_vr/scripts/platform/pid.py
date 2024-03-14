import numpy as np
import rospy


class PIDController:
    def __init__(self, kp: float, ki: float, kd: float, integral_limit = np.inf) -> None:
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.ilim = integral_limit

        self.last_err = 0
        self.isum = 0
        self.last_t = rospy.get_time()

    def zero(self):
        """
        Zero the integral value
        """
        self.isum = 0
        self.last_err = 0
        self.last_t = rospy.get_time()

    def step(self, error: float) -> float:
        """
        Step the pid controller.
        """
        c_t = rospy.get_time()
        delta_t = c_t - self.last_t
        self.last_t = c_t
        self.isum =  np.clip(self.isum  + error * delta_t, -self.ilim, self.ilim)
        value = self.kp * error + self.ki * self.isum + self.kd * (error - self.last_err) / delta_t
        self.last_err = error
        return value
