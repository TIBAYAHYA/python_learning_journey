import sys,webbrowser,pyperclip
if len(sys.argv) > 1:
    adress = " ".join(sys.argv[1:])
else:
    adress = pyperclip.paste()
webbrowser.open("https://google.com/maps/place/"+adress)
