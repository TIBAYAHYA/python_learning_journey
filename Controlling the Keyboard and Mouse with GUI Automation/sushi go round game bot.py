"""this program is supposed to play the web game <sushi go round><https://www.crazygames.fr/jeu/sushi-go-round> automaticly and efficiently for the user,
25/01/2025 2:07 AM UPDATE: this project took longer than It should have, some dumb mistakes have been made by me, leading to an infinite tryal of fixing a non existent mistake, almost gave up on the whole thing,
but thankfuly found out where the problem lays
"""
import pyautogui,time,os,logging
logging.basicConfig(level=logging.DEBUG)  

#logging.disable(logging.debug)  #uncomment to disable debugs
ingredients_folder_path = r"C:\Users\maroc\OneDrive\Desktop\sushi go round images\ingredients"
orders_folder_path = r"C:\Users\maroc\OneDrive\Desktop\sushi go round images\orders"




#a function that consistenly trys to open the target window


recipes = {
    "onigiri":["rice","rice","nori"],
    "roll":["rice","nori","fish"],
    "maki":["rice","nori","fish"]
    

}


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

    ingredients_locat = {}  #dictionaire of every ingredient and Its coordinates


  #we walking over the ingredients images file
    for filename in os.listdir(ingredients_folder_path):
            
        ingredienta = filename[:-10]  # keep only the meaningful part of the file name
        while True:
            try:
                ingredients_locat[ingredienta] = pyautogui.locateCenterOnScreen(os.path.join(ingredients_folder_path,filename),confidence=0.9)  #we assign each ingredients an opposition coordinates in the form of a dictionary
                ingredients_locat[ingredienta] = (int(ingredients_locat[ingredienta].x),int(ingredients_locat[ingredienta].y))
                break
            except pyautogui.ImageNotFoundException: # try except loop to make sure It keeps trying until image matchs
                logging.debug("could not find: ",ingredienta," trying again...")
                time.sleep(1)
    return ingredients_locat



 #a function for taking orders, might want to adjust the conf value depending on how often orders dont get detected, but for now It seems to be erreur prone
def take_orders():

    take_orders_dict = {}   # this is the dictionary where we gonna assign number of orders

    for filename in os.listdir(orders_folder_path):
            image_real_path = os.path.join(orders_folder_path,filename)
            ingredient_name = filename[:-4]

            try:
                if ingredient_name == "roll":
                    conf = 0.85
                elif ingredient_name == "maki":
                    conf = 0.94
                elif ingredient_name == "onigiri":
                    conf =0.9
                take_orders_dict[ingredient_name] = len(list(pyautogui.locateAllOnScreen(image_real_path,confidence=conf,region=(483,250,1267,322)))) # this makes in place every order with number of orders

                
            except Exception:
                    take_orders_dict[ingredient_name] = 0 #in case of exception, which is probably an image not found, assign 0 to number of orders

    return take_orders_dict

def prepare_orders(to_cook_dict):
    try:
        for to_cook in to_cook_dict.keys():
            if to_cook_dict[to_cook] != 0:
                for cooking_times in range(to_cook_dict[to_cook]):
                    for singular_recipe in recipes[to_cook]:
                        pyautogui.click(ingredients_locat[singular_recipe])
                
                    pyautogui.click(table_location)
                    time.sleep(1)
    except AttributeError:
        time.sleep(1)












actv_game()

os.chdir(r"C:\Users\maroc\OneDrive\Desktop\sushi go round images")
find_on_screen("Blue_PlayButton.png") #play button 
find_on_screen("Yellow_SkipButton.png") #skip tutorial button
find_on_screen("Purple_ContinueButton.png") #first stage button

ingredients_locat = locate_ingredients_coordinates() # a dictionary that contains every recipe's coordinates

# a while loop that stores the location of table in a variable, may need to change confidence later...
while True:
    try:
        table_location = pyautogui.locateCenterOnScreen(r"C:\Users\maroc\OneDrive\Desktop\sushi go round images\table.png")
        break
    except pyautogui.ImageNotFoundException:
        logging.debug("no table was found")
        time.sleep(1)


while True: #have to change this later into a conition that checks for level end (win/lose) situation

    orders = take_orders()
    logging.debug(take_orders)
    prepare_orders(orders)
    time.sleep(5)









