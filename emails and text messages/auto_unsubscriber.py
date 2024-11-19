"""this program is supposed to iterate over my entire email list, find unsubscribe links, and automaticly opens them in browser

"""
exclude_domains = ["https://www.youtube.com", "https://twitter.com"]
import imapclient
import webbrowser
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email = input("Enter your Email: ")
password = input("Enter Your Passsword: ")
conn.login(email,password)
conn.select_folder("INBOX",readonly=True)  #INBOX folder, and read only to not risk deleting stuff
messages_IDS = conn.search(["ALL"])  #a list of all emails IDS
unsubscribe_links = []  #later to be used list

import pyzmail,bs4

for message_ID in messages_IDS:
 #every single message id
    print("Traiting message: %s"%(message_ID))
    raw_msg = conn.fetch([message_ID],["BODY[]","FLAGS"])   #fetching the message
    message = pyzmail.PyzMessage.factory(raw_msg[message_ID][b"BODY[]"])#parsing the message
    if message.html_part: #checking If the message is html
        html_content = message.html_part.get_payload().decode(message.html_part.charset if message.html_part.charset else "utf-8") #getting the html content
        #bs4ing
        soup = bs4.BeautifulSoup(html_content,"html.parser")
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if 'unsubscribe' in link.get_text().lower() or 'unsubscribe' in link.get('href', '').lower(): #checking If the html  "a" has
        #bs4ing        
                if  not any(href.startswith(domain)for domain in exclude_domains): #youtube links are not unsubscribe links 
                    webbrowser.open(link.get('href'))  #opening the link in the browser




