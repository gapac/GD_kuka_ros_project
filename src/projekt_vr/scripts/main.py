#!/usr/bin/python3
"""
Main node file for Kuka mobile platform and arm.
"""

from robot import *

platform = Platform("/project_kuka/platform", MobileController(), LaserScanner(zero_angle_index=270))
platform.init_node()
platform.wait_ready()
platform.track_closest_object(min_distance=0.05, max_distance=2, target_x=0.5)

# from gui import *
# from robot import *

# import tkinter.ttk as ttk
# import tkinter as tk


# class App:
#     def __init__(self) -> None:
#         self.root = tk.Tk()
#         self.root.title("Kuka mobile platform controller")

#         # Mobile platform objects
#         self.plt = Platform("platforma", MobileController(), LaserScanner())

#         # GUI
#         self.ctrl_panel = ControlPanel(self.plt, self.root)
#         self.ctrl_panel.pack()

#     def open(self):
#         self.root.mainloop()



# App().open()



