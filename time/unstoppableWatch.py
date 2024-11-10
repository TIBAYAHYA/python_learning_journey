"""just a stop watch that keeps track of the times between your "ENTER" key inputs, simple but effective
"""
""" 2nd updates, this time Im making the output of the code loke more readable or more 'pretty' for the reader,
    Im also adding a pyperclip.copy() method in case the user wants to quickly have the code's output in his availability
"""
import time
print("Press ENTER to start the clock, or CTRL+C to exit")
input()
print("Started")
start_time = time.time()
last_time = start_time
lap_num = 0
import pyperclip

try:
    while True:
        input()
        total_time = round(time.time()-start_time,2)
        
        
        
        lap_time = round(time.time()-last_time,2)
        last_time = time.time()

        lap_num += 1

        
        
        initial_string = f"Lap #{str(lap_num).rjust(2," ")}:{str(total_time).rjust(7," ")} ({str(lap_time).rjust(6," ")}) " #cool formating
        print(initial_string)
        pyperclip.copy(initial_string)   #copying the string into clip board 
        
        
except KeyboardInterrupt:   #keyboard interrupt exception message
    print("\nDone")
        