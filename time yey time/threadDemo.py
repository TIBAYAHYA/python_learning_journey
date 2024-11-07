import time,threading
print("Start of program")
def took_a_nap():
    time.sleep(5)
    print("WAKE UP!")
threading0bj = threading.Thread(target=took_a_nap)
threading0bj.start()
print("End of program")