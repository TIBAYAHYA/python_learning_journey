"""this a countdown program, give It a number of seconds and It will start counting down from It, and when timer reachs 0 some alarm sound will run!
"""
time_It = int(input("Enter the amount of Second:\n"))

import time
while time_It > 0:
    print(time_It,end = " ")
    time_It -= 1
    time.sleep(1)
import subprocess
process = subprocess.Popen(["start","alarm.wav"],shell=True)
process.wait()
