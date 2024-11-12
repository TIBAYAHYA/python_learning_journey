import imapclient
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email_a = input("Enter your email: ")
password_a = input("Enter your password: ")
counta = conn.login(email_a,password_a)
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
UIDs = conn.search(["ON","11-Nov-2024"]) #list all messages received ON x date
conn.delete_messages([UIDs]) #delete all emails that appear on the UIDs list, can also just give 1 email code aka something like nnnn (n is decimal number)



conn.logout()