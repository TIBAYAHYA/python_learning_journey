"""this program is supposed to use pyautogui to draw a spiral
"""
import pyautogui
import time
time.sleep(3) #delay allowing user to go into his drawing tab
distance = 500
while distance > 0:
    pyautogui.drag(distance,0) #top left
    distance = distance - 1
    pyautogui.drag(0,distance)  #top right
    pyautogui.drag(-distance,0) #bottom right
    distance = distance - 1
    pyautogui.drag(0,-distance) #bottom left