time_It = int(input("Enter the amount of Second:\n"))

import time
while time_It > 0:
    print(time_It,sep=" ")
    time_It -= 1
    time.sleep(1)
import subprocess
process = subprocess.Popen(["start","alarm.wav"],shell=True)
process.wait()