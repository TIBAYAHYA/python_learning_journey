"""very simple remake of the resize and add logo program, smoother and better!
"""
import os
from PIL import Image
image_files = [file for file in os.listdir(".") if file.lower().endswith(".png")or file.lower().endswith(".jpg")or file.lower().endswith(".gif")]
image_files.remove("logo.png") #remove the logo file
logo_open = Image.open("logo.png") 
logo_width,logo_height = logo_open.size
print(image_files)
for image_file in image_files:
    img_open = Image.open(image_file)
    width,height = img_open.size
    if width < 300: #width resizing
        width = 300
        img_open = img_open.resize((width,height))
    if height < 300:
        height = 300 #heigh resizing
        img_open = img_open.resize((width,height))
    img_open.paste(logo_open,(width-logo_width,height-logo_height),logo_open)  # we want logo to be located on bottom right of img
    img_open.save(image_file)