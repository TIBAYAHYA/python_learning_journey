"""this program is supposed to play the web game <sushi go round><https://www.crazygames.fr/jeu/sushi-go-round> automaticly and efficiently for the user,

"""
import pyautogui,time,os
os.chdir(r"C:\Users\maroc\OneDrive\Desktop\sushi go round images")


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
            








 
            
actv_game()

find_on_screen("Blue_PlayButton.png") #play button 

find_on_screen("Yellow_SkipButton.png") #skip tutorial button

find_on_screen("Purple_ContinueButton.png") #first stage button










