""" This program is supposed to check the website of (mutiple) web comics and If It have been updated, the comic gets downloaded into desktop
Im use the website xkcd.com as the only example, but It is gonna be easy to replicate on other websites, so long that you can bs4 them,
the main concept that we are trying to learn
""" 

def daily_timer():
    import time
    import datetime
    while True:
        if datetime.datetime.now().hour == 19 and datetime.datetime.now().minute == 55:
            comic_daily_checker()
            
        else:
            time.sleep(60)



def comic_daily_checker():
    import os
    os.makedirs("target comics",exist_ok=True)
    list_of_comics_websites = ["https://xkcd.com"]
    import requests,bs4
    for website in list_of_comics_websites:
        req = requests.get(website)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"html.parser")
        comic_elem = soup.select("#comic img") # first selection to get img tags
        comic_url = comic_elem[0].get("src")   #second selecting to get actual url
        img_req = requests.get("https:%s" % comic_url) # true img download url
        req.raise_for_status()
        for img_file in os.listdir("target comics"):
            if img_file == os.path.basename(comic_url):
                print("comic already downloaded")
                import time
                time.sleep(60)
                daily_timer()
        image_file_name = os.path.join("target comics",os.path.basename(comic_url)) #file name yeah
        image_file = open(image_file_name,"wb")#open img file in write binary mode
        for chunk in img_req.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        print("comic downloaded: %s" % os.path.basename(comic_url))
        time.sleep(60)
        
        
    daily_timer()
    

daily_timer()
    