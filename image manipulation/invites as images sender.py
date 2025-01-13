"""this program is supposed to make to make a list of invite lists, similar to docx program, but this time with images
"""
from PIL import Image,ImageDraw,ImageFont
import os

os.makedirs("guests folder", exist_ok=True) #folder to store the invites imgs
os.chdir(os.path.join(os.getcwd(),"guests folder"))
guests_file = open(r"C:\Users\maroc\Downloads\automate_online-materials\guests.txt", "r")
guests_list = guests_file.read().split("\n")  # making a list of the txt content
flower = r"C:\Users\maroc\OneDrive\Desktop\coding journey\python\image manipulation\flower.jpg" # the flower image that will be used as a template
font1 = ImageFont.truetype(os.path.join(r"C:\Windows\Fonts","arial.ttf"),17) #first font
font2 = ImageFont.truetype(os.path.join(r"C:\Windows\Fonts","tahoma.ttf"),23) #second font
font3 = ImageFont.truetype(os.path.join(r"C:\Windows\Fonts","verdana.ttf"),25) #third font
x = 20 # fixed x coordinate of the text
for guest in guests_list:  #iterate over the guests
    flower_image = Image.open(flower)  #iterate over image opening to avoid txt clutter
    draw = ImageDraw.Draw(flower_image)
    ### text drawing process
    draw.text((x,100),"You have been invited!",font=font1,fill="black")
    draw.text((x,130),f"Dear {guest}",font=font2,fill="black")
    draw.text((x,160),"we could like to have you join us",font=font1,fill="black")
    draw.text((x,190),"on the 25th of December",font=font2,fill="black")
    draw.text((x,220),"at our place",font=font2,fill="black")
    draw.text((x,250),"at 7:00 PM",font=font2,fill="black")
    flower_image.save("invite for "+guest+".jpg")
    ###
