""" This program is supposed to copy the text content of a window that is already open in the computer, save It in a pastable form, and then do something with it(print for now)
"""
import pyautogui,pyperclip
window_name = "New Text Document.txt - Notepad"  #title of the target window

target_window = pyautogui.getWindowsWithTitle(window_name) #window objects lists

target_window = target_window[0] #isolation of the window object

target_window.activate()  #activating the window

###
#some code to find the middle of the window, I know there is probably a command to straight up get the middle pixel of an opened window
import time
time.sleep(0.5) # half a second delay to make sure commands register
initial_x = (target_window.bottomright[0] - target_window.topleft[0]) /2

initial_y = (target_window.bottomright[1] - target_window.topleft[1]) /2

x = target_window.topleft[0] + initial_x
y = target_window.topleft[1] + initial_y
#####

pyautogui.click(x,y) #clicking the middle of the window
pyautogui.hotkey("ctrl","a") #selecing everything
pyautogui.hotkey("ctrl","c") #copying what is selected
copyed_text = pyperclip.paste() #saving the copyed text into a variable
target_window.minimize()
print(copyed_text)




