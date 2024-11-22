"""this is some testing of image manipulation stuff, mainly the pillow module, also known as PIL
"""
from PIL import Image
import os
cwd = os.getcwd()
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
zophie_img = Image.open("zophie.png")
print(zophie_img.size)
cropped_zophie = zophie_img.crop((335, 345, 565, 560))
os.chdir(cwd)
cropped_zophie.save("cropped_zophie.png")