""" this is some testing on how to insert texts into an img file, with context of image manipulation
    will be doing the project tomorrow, In case Im not so tight on uni work(Im not sure If I will be able to do It tomorrow)
"""
from PIL import Image,ImageFont,ImageDraw
import os
im = Image.new("RGB",(200,200),"white")
draw = ImageDraw.Draw(im)
draw.text((20,20),"Hello World",fill="black")
#1 this is the fonts folder, usually located at C:\Windows\Fonts, but we give It that name and so the program is smart enough to find It
#2 the font name
#3 the font size
                                              #1             #2        #3
arialFont = ImageFont.truetype(os.path.join("FONT_FOLDER","arial.ttf"),32) # font variable that we will use to write text

#1 the position of the text
#2 the text
            #1       #2                                
draw.text((20,50),"Hello World",font=arialFont,fill="black")  # the actual text writing, we use font variable HERE and some more
im.save("text drawing.png")