#Countdown Timer Python Project
# you will learn how to build a countdown timer using the time Python module. 
# This is a great beginner project to get you used to working with while loops in Python.

import time


second = int(input("How many seconds for the countdown ? "))
while second > 0 :
    print(second)
    time.sleep(5)
    second -= 1

print("time's up ! ")     