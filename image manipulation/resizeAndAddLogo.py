""" this program is supposed to add a logo to every single image in cwd
"""
import os
from PIL import Image
os.makedirs("dump folder",exist_ok=True)
images_to_modify = [file for file in os.listdir(".") if file.endswith(".png")]
for image_name in images_to_modify:
    image_open = Image.open(image_name)
    width,height = image_open.size
    if width < 300:
        width = 300
        image_open.resize(300,height)
    if height < 300:
        height = 300
        image_open.resize(width,300)
    image_name_tuple = image_name[:-4],"_Logoed",image_name[-4:]
    file_new_name = "".join(image_name_tuple)
    print(file_new_name)
    file_name = os.path.join(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\image manipulation\dump folder",file_new_name)
    print(file_name)
    image_open.save(file_name)