"""this program is supposed to continously simulate mouse mouvements to prevent triggering the idle tracker in some application, used some randomization factor to make sure the pattern doesnt get easily tracked
"""
import pyautogui,time,random
while True:
    x = random.randint(-5,5)
    y = random.randint(-5,5)
    time.sleep(10)
    pyautogui.move(x,y)

