"""this is some testing of image manipulation stuff, mainly the pillow module, also known as PIL
"""
from PIL import Image
import os
cwd = os.getcwd()
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
zophie = Image.open("zophie.png")
os.chdir(cwd)
zophie_face = Image.open("zophie_face.png")
zophie_width,zophie_height = zophie.size 
zophie_face_width,zophie_face_height = zophie_face.size
for top in range(0,zophie_height,zophie_face_height):
    for left in range(0,zophie_width,zophie_face_width):
        zophie.paste(zophie_face,(left,top))
        print(left,top)
zophie.save("cat_invasion.png")

