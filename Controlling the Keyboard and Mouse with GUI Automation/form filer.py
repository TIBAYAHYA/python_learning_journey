import pyautogui
import sys
import time

first_click = 697, 422
formData = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]

try:
    print("You have 5 seconds to tab into the form...")
    time.sleep(5)  # 5 seconds delay, to give the user an option of quitting before the execution starts

    for form_element in formData:
        pyautogui.click(first_click)  # First click on the screen, also gonna be location of the name element
        pyautogui.write(form_element["name"])  # Writing name
        pyautogui.press("tab")  # Going into the next step
        pyautogui.write(form_element["fear"])  # Writing fear
        pyautogui.press("tab")  # Tab to next field
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("down")
        time.sleep(0.5)  # Small delay to ensure the dropdown opens
       
        if form_element["source"] == "amulet":
            pyautogui.press("down")
        if form_element["source"] == "crystal ball":
            pyautogui.press("down")
            pyautogui.press("down")
        if form_element["source"] == "money":
            pyautogui.press("down")
            pyautogui.press("down")
            pyautogui.press("down")


        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("tab")  # Moving to next tab
        pyautogui.press("down")  # Initial down to focus robocop rating

        # Robocop "grading"
        if form_element["robocop"] == 1:
            pyautogui.press("up")
        elif form_element["robocop"] == 3:
            pyautogui.press("down")
        elif form_element["robocop"] == 4:
            pyautogui.press("down")
            pyautogui.press("down")
        elif form_element["robocop"] == 5:
            pyautogui.press("down")
            pyautogui.press("down")
            pyautogui.press("down")

        pyautogui.press("tab")  # Moving to next tab
        pyautogui.press("tab")  # Comment accessing
        pyautogui.write(form_element["comments"])  # Writing comment
        pyautogui.press("tab")  # Tab to the next field
        pyautogui.press("enter")  # Press Enter to submit
        time.sleep(1)  # Small delay before moving to the next form
        pyautogui.press("tab")  # Another tab
        pyautogui.press("enter")  # Final submit
        time.sleep(1)  # Small delay before moving to the next form

except KeyboardInterrupt:  # In case of user quitting
    print("Exiting...")
    sys.exit()