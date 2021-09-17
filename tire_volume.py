# File name: tire_volume.py
# Author: Amon Brollo

import math

# v is the volume in liters,
# π is the constant PI which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")
