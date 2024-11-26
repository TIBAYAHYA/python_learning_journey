"""this is a program that iterates across the entire hard drive and finds folders that contain more images than non-image files, images as of ends with .pn
It then writes the path of the folder to a log file.
"""
import os
from PIL import Image

log_file = open(r'C:\Users\maroc\OneDrive\Desktop\log.txt', 'w')  #recreating the file each time we run program to avoid duplicates
log_file.close()
for foldername, subfolders, filenames in os.walk('C:\\'): #the crawling
    log_file = open(r'C:\Users\maroc\OneDrive\Desktop\log.txt', 'a')
    print('The current folder is: ' + foldername) #current folder showcase
    NuMof_NonImg=0
    NumOf_Imgs = 0
    for filename in filenames:
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            NuMof_NonImg += 1
            continue
        open_file = Image.open(os.path.join(foldername, filename))
        width, height = open_file.size
        if width < 500 or height < 500: # width and height of the image must be above 500
            NuMof_NonImg += 1
            continue
        NumOf_Imgs += 1
    if NumOf_Imgs > NuMof_NonImg:
        log_file.write("The folder is an Image folder: "+foldername+"\n") #writing into the log file
        log_file.close()
    
        
        
