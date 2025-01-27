
"""first time, I partialy followed the book insructions, but It kept on redownloading some files more than once, and so I decided to take matters into my own hand
and write the whole code from nothing
"""

"""my second try at the threading object, I rewrote the whole thing, exept this time things seem to work perfectly,also added a variable that keeps track
of the latest comic added before starting the process
""" 
#this time It works perfectly!!!
#side note: make sure to terminate the program and not let It run for so long, unless you are fine with downloading thousands of comic images :)
import requests,os,bs4

#this process should keep track of the latest added comic
req = requests.get("https://xkcd.com")
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text,"html.parser")
first_select = soup.find('meta', property='og:url')
second_select = first_select['content'].strip('/').split('/')[-1] #returns the latest comic number

second_select = int(second_select)
##############################################
os.makedirs("xkcd",exist_ok=True)
def download_xkcd(start_comic,end_comic):
    for comicNumber in range(start_comic,end_comic):
        req = requests.get("https://xkcd.com/%s"%(comicNumber)) # requesting the web page
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"html.parser") # soup element parsed
        comic_elem = soup.select("#comic img") # first selection to get img tags
        if comic_elem == []:
            print("could not find comic image of %s"%(comicNumber))
            
        else:
            comic_url = comic_elem[0].get("src")   #second selecting to get actual url
            print("downloading image %s"%(comic_url))
            req = requests.get("https:%s" % comic_url) # true img download url
            req.raise_for_status()
            image_file_name = os.path.join("xkcd",os.path.basename(comic_url)) #file name yeah
            
            image_file = open(image_file_name,"wb")#open img file in write binary mode
            for chunk in req.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
        if comicNumber == second_select:   #if the comic number is equal to the latest available comic, bro just leave
            import sys
            sys.exit()
            
            

import threading

for i in range(0,second_select,10):   #second_select is the latest available comic, we are gonna download comics 10 by 10, the comment above
                                      #explains how we gonna avoid the code crashing If last comic is not a multiplier of 10
    start = i
    end = i+9
    if start == 0 :
        start = 1
        
    download_thread_obj = threading.Thread(target=download_xkcd,args=(start,end))
    download_thread_obj.start()
    