import os,send2trash
for file in os.listdir("."):
    if file.endswith("csv"):
        send2trash.send2trash(file)