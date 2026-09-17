"""
Target Heart Rate Calculator
Author: Conner Allen
Title: Target Heart Rate Calculator
Description:
This program calculates a person's maximum
heartrate and the target heart rate ranges
for moderate and vigorous activities based on the user's age
"""

# INPUT
# Prompt the user to enter their age in years
age = int(input("Enter your age in years: "))

# PROCESSING
# Calculate maximum heart rate
max_heart_rate = 220 - age

# Calculate target heart rate ranges
moderate_low = max_heart_rate * 0.50
moderate_high = max_heart_rate * 0.70
vigorous_low = max_heart_rate * 0.70
vigorous_high = max_heart_rate * 0.85

# OUTPUT
# Display results to user
print(f"For age = {age} years,")
print(f"Maximum heart rate = {max_heart_rate} bpm")
print(f"Target heart rate for moderate activity = {moderate_low} to {moderate_high} bpm")
print(f"Target heart rate for vigorous activity = {vigorous_low} to {vigorous_high} bpm ")