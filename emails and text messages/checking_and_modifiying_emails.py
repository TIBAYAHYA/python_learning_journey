"""this is a bunch of code I wrote as Im learning the imapclient and pyzmail libs, the libs seem complicated, there is prolly a smother alternative,
but for now we gonna learn the hard way and experiment with this old library
"""


import imapclient
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email_a = input("Enter your email: ")
password_a = input("Enter your password: ")
conn.list_folders()  #returns a list of folder,(you dont have to constantly tell me that I have no children)
conn.select_folder("INBOX",readonly=True)  #folder selection in read only mode
UIDs = conn.search(["SINCE", "01-Nov-2024"])   #returns a list of email numbers that can be used below!
raw_msg = conn.fetch([6200],["BODY[]","FLAGS"])   #6200 is an email number
import pyzmail
message = pyzmail.PyzMessage.factory(raw_msg[6200][b"BODY[]"]) #returns a few things
message.get_subject()  #email subject
message.get_addresses("from") #source of email adress, first list element is the name, second is the email adress
message.get_addresses("to")   # email adress of the receiver, first list element is the name, second is the email adress
message.get_address("bcc")    #
message.html_part    #boolean for => Is the message a html?
message.text_part    #boolean for => Is the message a text?
message.html_part.get_payload().decode("UTF-8")   #text of the email
#example of deleting folders
conn.select_folder("INBOX",readonly=False) #folder selection in read only mode being off
UIDs = conn.search(["ALL"]) #list all messages received ON x date
#conn.delete_messages([UIDs]) #delete all emails that appear on the UIDs list, can also just give 1 email code aka something like nnnn (n is decimal number)
"""since alot of emails, and I mean ALOOOT OF EMAILS, are in html format, and I couldnt find one
in txt format, I made a program that check my entire inbox and finds 1 singular gmail in txt format than exits out
"""


import sys
rawer_message = conn.fetch([521],["BODY[]","FLAGS"])
messaga = pyzmail.PyzMessage.factory(rawer_message[521][b"BODY[]"])



print(messaga.text_part.get_payload().decode("UTF-8"))
sys.exit()
    
conn.logout()
"""finnaly found a text email!!! but Its past midnight and I missed some github daily upload points
   plus I need to sleep
"""