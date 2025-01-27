" same countdown, exept this time It has the cancel opetion with try, exept statement"

time_It = int(input("Enter the amount of Second:\n"))
print("Press CTRL-C to cancel",sep="\n")
import time
try:
    while time_It > 0:
        print(time_It,end=" ")
        time_It -= 1
        time.sleep(1)
    import subprocess
    process = subprocess.Popen(["start","alarm.wav"],shell=True)
    process.wait()
except KeyboardInterrupt:
    import sys
    sys.exit()
