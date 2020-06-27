"""
Refactor Code Example
"""

total_seconds = int(input("Enter total seconds: "))

hours = str(int(total_seconds / 3600))
minutes = str(int(total_seconds / 60) % 60)
seconds = str(total_seconds % 60)

if len(minutes) < 2 and hours != "0":
    minutes = "0" + minutes
if len(seconds) < 2:
    seconds = "0" + seconds
time = minutes + ":" + seconds
if hours != "0":
    time = hours + ":" + time

print(f"Formatted Time = {time}")
