""" this program is supposed to add a logo to every single image in cwd that has the .png extension
"""
import os
from PIL import Image

os.makedirs("dump folder", exist_ok=True)
images_to_modify = [file for file in os.listdir(".") if file.endswith(".png")] #selecting files that end with .png extension

logo = Image.open("logo.jpg") # the logo file
logo_width, logo_height = logo.size

for image_name in images_to_modify:
    image_open = Image.open(image_name)
    width, height = image_open.size  # width and height attributes
    ### resizing in case the image is below 300 width of height
    if width < 300:
        width = 300
        image_open = image_open.resize((width, height))
    if height < 300:
        height = 300
        image_open = image_open.resize((width, height))
    ###
    
    image_name_tuple = image_name[:-4], "_Logoed", image_name[-4:]  # new name, remove extension, add _logoed and add the extension again
    file_new_name = "".join(image_name_tuple)
    image_open.paste(logo,(width -logo_width, height - logo_height))   #paste the logo into the 
    
    file_name = os.path.join(r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\image manipulation\dump folder", file_new_name) # joining file name with target folder location
    print(file_name)
    image_open.save(file_name) # saving the file USING absolute path, just to make sure