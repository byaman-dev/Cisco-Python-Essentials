# File: 06_time_converter.py
# Objective: Convert total seconds into Hours, Minutes, and Seconds.

total_seconds = int(input("Enter total seconds: "))

# Calculate hours, then the remainder
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

# Calculate minutes from the remainder
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"Time is: {hours}h : {minutes}m : {seconds}s")
