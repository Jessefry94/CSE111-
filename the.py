# CSE 111 by Jesse Fry
import math
import datetime
# w = int(input("Enter the width of the tire in millimeters: "))
# a = int(input("Enter the aspect ratio of the tire: "))
# d = int(input("Enter the diameter of the wheel in inches: "))

# v = (math.pi * ({w}**2) * {a}) * ({w} * {a} + (2540 * {d}))/ 10000000000
def compute_data(w, a, d):
    return (math.pi * (w**2) * a) * (w * a + (2540 * d))/ 10000000000
print(compute_data(185, 50, 14))
print(compute_data(205, 60, 15))


current_date_and_time = datetime.datetime.now()
print(f"The current date is: {current_date_and_time:%y-%m-%d}")
print("The time is now: " + (current_date_and_time.strftime("%I:%M:%S%p")))

with open("volumes.txt", "at") as volume_file:
    print(f"{volume_file}")