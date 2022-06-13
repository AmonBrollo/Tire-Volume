# File name: tire_volume.py
# Author: Amon Brollo

import math
from datetime import datetime

# v is the volume in liters,
# π is the constant PI which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

current_date = datetime.now()

print(f"The approximate volume is {v:.2f} liters")

wants_to_buy = input("Would you like to buy tires with the entered dimensions?(Yes/No) ")
if wants_to_buy.lower() == "yes":
    phone_number = input("Please enter your phone number: ")

with open("volumes.txt", "at") as file:
    print(f"Current date: {current_date:%Y-%m-%d}", file=file)
    print(f"Width of the tire: {w:.0f}", file=file)
    print(f"Aspect ratio of the tire: {a:.0f}", file=file)
    print(f"Diameter of the wheel: {d:.0f}", file=file)
    print(f"Volume of the tire: {v:.2f}", file=file)
    print(f"Phone number: {phone_number}\n", file=file)
