#!/usr/bin/python3
"""
Main node file for Kuka mobile platform and arm.
"""

from robot import *

platform = Platform("/project_kuka/platform", MobileController(), LaserScanner(zero_angle_index=270))
platform.track_closest_object(min_distance=0.05, max_distance=2, target_x=0.5)
