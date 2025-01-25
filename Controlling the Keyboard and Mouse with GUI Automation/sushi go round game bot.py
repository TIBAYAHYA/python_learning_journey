"""this program is supposed to play the web game <sushi go round><https://www.crazygames.fr/jeu/sushi-go-round> automaticly and efficiently for the user,
25/01/2025 2:07 AM UPDATE: this project took longer than It should have, some dumb mistakes have been made by me, leading to an infinite tryal of fixing a non existent mistake, almost gave up on the whole thing,
but thankfuly found out where the problem lays
"""
import pyautogui,time,os,logging
logging.basicConfig(level=logging.DEBUG)  

#logging.disable(logging.debug)  #uncomment to disable debugs


#a function that consistenly trys to open the target window

def actv_game():
    while True:
        try:
            game_window = pyautogui.getWindowsWithTitle("Sushi Go Round 🕹️ Joue sur CrazyGames! - Google Chrome")
            game_window = game_window[0]
            print(game_window)
            game_window.activate()
            game_window.maximize()
            break
        except IndexError:
            print("Window Not Found")
            time.sleep(1)
    



 #this function actively searchs for an image on the screen, locates Its center and clicks It before breaking through
def find_on_screen(image_fileName):
    #
    while True:
        try:
            image_center = pyautogui.locateCenterOnScreen(image_fileName,confidence=0.9)  #this new confidence thing is some kind of image differentiation tolerance? I guess

            if image_center != None: #we only reach this point when no exception is raised
                pyautogui.click(image_center)
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(0.2)
            




#this function finds the coordinates of every ingredient
def locate_ingredients_coordinates():  
    global ingredients_locat
    ingredients_locat = {}  #dictionaire of every ingredient and Its coordinates


    for dirpath, dirnames, filenames in os.walk(r"C:\Users\maroc\OneDrive\Desktop\sushi go round images\ingredients"): #we walking over the ingredients images file
            for filename in filenames:
                    
                ingredienta = filename[:-10]  # keep only the meaningful part of the file name
                while True:
                    try:
                        ingredients_locat[ingredienta] = pyautogui.locateCenterOnScreen(os.path.join(dirpath,filename),confidence=0.9)  #we assign each ingredients an opposition coordinates in the form of a dictionary
                        break
                    except pyautogui.ImageNotFoundException: # try except loop to make sure It keeps trying until image matchs
                        print("could not find: ",ingredienta," trying again...")
                        time.sleep(1)













actv_game()

os.chdir(r"C:\Users\maroc\OneDrive\Desktop\sushi go round images")
find_on_screen("Blue_PlayButton.png") #play button 
find_on_screen("Yellow_SkipButton.png") #skip tutorial button
find_on_screen("Purple_ContinueButton.png") #first stage button

locate_ingredients_coordinates()
logging.debug(ingredients_locat)












