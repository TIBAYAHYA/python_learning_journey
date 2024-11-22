"""this is some testing of image manipulation stuff, mainly the pillow module, also known as PIL
"""
from PIL import Image
import os
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
cat_img = Image.open("zophie.png")
print(cat_img)