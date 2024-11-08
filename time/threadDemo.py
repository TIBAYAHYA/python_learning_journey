"""simple threading lib demo, this threading thing remouves one of python's weakness, making It able to execute multiple lines of code at same time
 yaaaay!!! lets go!!!
"""
import time,threading
print("hello people")
def threading_sample():
    time.sleep(5)
    print("hola amigo")
threading_obj = threading.Thread(target=threading_sample)
threading_obj.start()
print("bonjour my friend")