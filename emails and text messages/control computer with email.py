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
key_word = "Magito_the_idiot"




initial_UIDS = conn.search(["SINCE",formated_date])


import sys###



import time,pyzmail
def emails_checker():
    deleting_list = []
    conn.select_folder("INBOX",readonly=False)
    
    updated_uids = conn.search(["SINCE",formated_date])
    
    updated_uids = [uid for uid in updated_uids if uid not in initial_UIDS]
    
    

        
        
    if not updated_uids:
        print("No new emails")
        return
    for new_uid in updated_uids:
        raw_msg = conn.fetch([new_uid],["BODY[]","FLAGS"])   #fetching the message
        message = pyzmail.PyzMessage.factory(raw_msg[new_uid][b"BODY[]"])#parsing the message
        if not message.text_part:
            deleting_list.append(new_uid)
            print("No text part found")
            continue
        email_content = message.text_part.get_payload().decode(message.text_part.charset)
        if key_word not in email_content:
            deleting_list.append(new_uid)
            print("No key word found")
            continue
        
        
                
            
    
    
    
    
      
while True:
    
    time.sleep(5)
    
    emails_checker()
