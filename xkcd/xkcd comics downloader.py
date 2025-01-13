import requests,os,sys,bs4,logging
url = "https://xkcd.com/"
while True:
    res = requests.get(url)
    os.makedirs('xkcd', exist_ok=True) 
    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.content,"html.parser")
    ########################################################################################################
    ########################################################################################################   
        img_tag = soup.select('img[src*="//imgs.xkcd.com/comics/"]')      
        if img_tag:
            img_src = img_tag[0]['src']
            img_url = "https:"+img_src
            print("Downloading image"+img_url)
            comic_res = requests.get(img_url)
            res.raise_for_status()
            imgFile = open(os.path.join('xkcd', os.path.basename(img_src)), 'wb')
            for chunk in comic_res.iter_content(100000):
                imgFile.write(chunk)
            imgFile.close()
            link = soup.select('a[rel="prev"]')
            href_value = link[0]['href']
            url = 'https://xkcd.com' + href_value
            if url == "https://imgs.xkcd.com/comics/house_inputs_and_outputs.png":
                ()
    if url.endswith("#"):
        break
sys.exit