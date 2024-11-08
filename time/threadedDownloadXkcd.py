import requests,os,bs4,threading
#a program that downloads multiple xkcd comics at the same time using threading lib
os.makedirs("xkcd",exist_ok=True)
def downloadXkcd(start_comic,end_comic):
    for urlNumber in range(start_comic,end_comic):
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        req = requests.get("https://xkcd.com/%s" % (urlNumber))
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text,"html.parser")
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("could not find comic image")
        else:
            comicUrl = comicElem[0].get("src")
            print("downloading image",comicUrl)
            req = requests.get("https:%s" % comicUrl) #request for img png
            req.raise_for_status()
            imageFile = open(os.path.join("xkcd",os.path.basename(comicUrl)),"wb")
            for chunk in req.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()         
downloadThreads =[]
for i in range(0,141,10):
    start = i
    end = i+9
    if start == 0 :
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd,args=(start,end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
print("done")