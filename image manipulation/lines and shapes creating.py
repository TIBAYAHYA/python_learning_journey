"""just some testing with the drawing method of image manipulation
"""
from PIL import Image,ImageDraw
####### line drawing
new_img = Image.new("RGBA", (200, 200),"white")
draw = ImageDraw.Draw(new_img)
draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill="black",width=20) #each arguments represents coordinates of a point in the line drawing object:                                                                     
                                                                         #[(first,point),(second,point),(third,point),(fourth,point),(fifth,point)] and so on...
draw.line([(0,0),(199,199)],fill="black",width=20)
new_img.save("line_drawing.png")



########### rectangle drawing
new_img = Image.new("RGBA", (200, 200),"white")
drawing = ImageDraw.Draw(new_img)
drawing.rectangle((20,20,180,180),fill="blue",outline="black")  # arguments are : (left, top, right, bottom) , fill is inside color and outline is border color
new_img.save("rectangle_drawing.png")

######### ellipse drawing
new_img = Image.new("RGBA", (200, 200),"white")
drawing = ImageDraw.Draw(new_img)
drawing.ellipse((0, 0, 150, 150), fill='red') #same arguments of a rectangle but the shape is an ellipse, (left,top,right,bottom), If width = height the result is a circle
                                              #to draw a circle, do somrthing like this: drawing.ellipse((0, 0, 150, 150), fill='red')
new_img.save("ellipse_drawing.png")          
######## polygon drawing
new_img = Image.new("RGBA", (200, 200),"white")
drawing = ImageDraw.Draw(new_img)
drawing.polygon(((50, 90), (90, 70), (100, 90), (130, 80), (110, 120)),fill='brown')  #same as draw line, exept the last pair of coordinates will be automaticly linked to 
                                                                                        #the first pair of coordinates to close the polygon
new_img.save("polygon_drawing.png")

######## for loop of drawing
new_img = Image.new("RGBA", (200, 200),"white")
drawing = ImageDraw.Draw(new_img)
for i in range(0, 200, 10):
    drawing.line([(i, 0), (200, i - 100)], fill='green')
new_img.save("for_loop_drawing.png")

    