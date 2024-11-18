"""this program is supposed to iterate over my entire email list, find unsubscribe links, and automaticly opens them in browser

"""
import imapclient
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email = input("Enter your Email: ")
password = input("Enter Your Passsword: ")
conn.login(email,password)
conn.select_folder("INBOX",readonly=True)
messages_IDS = conn.search(["ALL"])  #a list of all emails IDS
unsubscribe_links = []  #later to be used list

import pyzmail,bs4
for message_ID in messages_IDS:
    raw_msg = conn.fetch([message_ID],["BODY[]","FLAGS"])   #
    message = pyzmail.PyzMessage.factory(raw_msg[message_ID][b"BODY[]"])
    if message.html_part:
        html_content = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html_content,"html.parser")
        