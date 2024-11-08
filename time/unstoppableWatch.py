"""just a stop watch that keeps track of the times between your "ENTER" key inputs, simple but effective
"""
import time
print("Press ENTER to start the clock,or CTRL+C to exit")
input()
print("Started")
start_time = time.time()
last_time = start_time
lap_num = 0

try:
    while True:
        input()
        total_time = round(time.time()-start_time,2)
        
        lap_time = round(time.time()-last_time,2)
        last_time = time.time()

        lap_num += 1
        
        print(f"Lap #{lap_num} \ntotal time: {total_time} second.\nlap time: {lap_time} second.")
        
except KeyboardInterrupt:   #keyboard interrupt exception message
    print("\nDone")
        