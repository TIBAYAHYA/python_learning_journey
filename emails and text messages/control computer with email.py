"""

this program is supposed to check email every 15 minutes,for any emails sent as instruction
the program should also look up for a confirmation code to ensure no bad actors abuse the program
the program should delete emails after they are used to prevent repeating same instructions
as well as send a confirmation after the instruction is executed, or the error message in case the program failed

"""
#status: incomplete
import imapclient,datetime
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email = input("Enter your Email: ")
password = input("Enter Your Passsword: ")
conn.login(email,password)
conn.select_folder("INBOX",readonly=False)  #INBOX folder
start_now = datetime.datetime.now()
formated_date = start_now.strftime("%d-%b-%Y")




initial_UIDS = conn.search(["SINCE",formated_date])





import time,pyzmail
def emails_checker():
    if initial_UIDS:
        new_uids = conn.search(["SINCE",formated_date])
        for ini_uid in initial_UIDS:
            new_uids.remove(ini_uid)
    if not new_uids:
        print("No new emails")
        return
    for new_uid in new_uids:
        raw_msg = conn.fetch([new_uid],["BODY[]","FLAGS"])   #fetching the message
        message = pyzmail.PyzMessage.factory(raw_msg[new_uid][b"BODY[]"])#parsing the message
        if message.html_part:
            return
        email_content = message.text_part.get_payload().decode(message.text_part.charset)
        print(email_content)
                
    
    
    
    
      
while True:
    
    time.sleep(900)
    print("checking for emails") 
    emails_checker()
