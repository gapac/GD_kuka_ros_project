from robot import Platform, MobileController
from threading import Thread

from .hintedentry import *

import tkinter.ttk as ttk
import tkinter as tk
import rospy
import os


__all__ = ("ControlPanel",)


class Tracking:
    def __init__(self, platform: Platform) -> None:
        self.platform = platform
        self.running = False
        self.thread: Thread = None
    
    def run(self):
        self.thread = Thread(target=self.platform.track_closest_object)
        self.thread.start()

    def stop(self):
        self.platform.stop_tracking()
        if self.thread is not None:
            self.thread.join()


class ControlPanel(ttk.Frame):
    def __init__(self, platform: Platform, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.plt = platform

        self.entry_ros_host = HintedEntry("ROS Host / IP", self)
        self.entry_ros_host.pack()
        self.entry_ros_master = HintedEntry("ROS Master", self)
        self.entry_ros_master.pack()

        self.bnt_connect = ttk.Button(self, text="Connect", command=self._connect)
        self.bnt_connect.pack()

        self.bnt_connect = ttk.Button(self, text="Stop", command=self._stop)
        self.bnt_connect.pack()

        ttk.Separator(self).pack(fill=tk.X, pady=5)

        self.plt_tracking = Tracking(platform)
        self.bnt_track = ttk.Button(self, text="Track object", command=self.plt_tracking.run)
        self.bnt_track.pack()

    def _connect(self):
        e = os.environ
        e["ROS_MASTER"] = self.entry_ros_master.get()
        e["ROS_HOST"] = self.entry_ros_host.get()
        e["ROS_IP"] = e["ROS_HOST"]
        self.plt.init_node()

    def _stop(self):
        self.plt_tracking.stop()
        self.plt.mobile.stop_movement()
