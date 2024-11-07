import bs4,requests
exampleFile = open(r"C:\Users\maroc\OneDrive\Desktop\coding journey\html\example.html")
Soup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
spanElem = Soup.select("span")[0]
print(spanElem.get("id"))