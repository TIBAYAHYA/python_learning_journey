""" GUI automation stands for graphical user interface automation
"""

import pyautogui

pyautogui.move(-100,200,duration=1)#PYAUTOGUI.move(int,int,duration=float)  is move in relative to current mouse position ,
                                   #integer can be negative
pyautogui.moveTo(100,0,duration=0.25)     #PYAUTOGUI.moveTO(int,int,duration=float)  is move in absolute to screen resolution.
                 #coordinates cant be negative, unless you have a 3rd dimension screen

pyautogui.position() #grabs the current coordinates of mouse
pyautogui.click(100,100) #clicks on the coordinates, can also contain no coordinates, in which case it will click on current mouse position
pyautogui.click(100,100,button='right') #It can also contain button='left' or 'right' or 'middle'
pyautogui.doubleClick()#self explanatory


