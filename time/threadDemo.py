import time,threading
print("hello people")
def threading_sample():
    time.sleep(5)
    print("hola amigo")
threading_obj = threading.Thread(target=threading_sample)
threading_obj.start()
print("bonjour my friend")