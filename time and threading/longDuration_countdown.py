"""this time the prograss can deal with year/month/day based time inputs !
"""

import datetime


now = datetime.datetime.now()
future_date = datetime.date(2025,7,19)
time_difference = future_date - now.date()
seconds_left = time_difference.total_seconds()
secondas = seconds_left
try:
    import time
    print("Press CTRL-C to terminate the countdown")
    while secondas > 0:
        print(int(secondas)," Seconds Left for the Due Day!")
        secondas -= 1
        time.sleep(1)
    import subprocess
    popen_obj = subprocess.Popen("start","alarm.wav")   # no happy birthday music, sorry you gonna have to listen
                                                        #to this ugly alarm :'(
    popen_obj.wait()
except KeyboardInterrupt:
    print("Terminating the Porgram...")
    import sys
    sys.exit()

