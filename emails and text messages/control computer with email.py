"""

this program is supposed to check email every 15 minutes,for any emails sent as instruction
the program should also look up for a confirmation code to ensure no bad actors abuse the program
the program should delete emails after they are used to prevent repeating same instructions
as well as send a confirmation after the instruction is executed, or the error message in case the program failed

"""
#status: working
import imapclient,datetime
conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
email = input("Enter your Email: ")
password = input("Enter Your Passsword: ")
conn.login(email,password)
conn.select_folder("INBOX",readonly=False)  #INBOX folder
start_now = datetime.datetime.now()  #the now time
formated_date = start_now.strftime("%d-%b-%Y")   #correct format that gets accepted as a second argument of conn.search()
key_word = "Magito_the_idiot"        #keyword to be checked in each mail





initial_UIDS = conn.search(["SINCE",formated_date])  #searching for emails sent "today" according to time shot



### part that enables email sending
import subprocess,os
cwd = os.getcwd()
import time,pyzmail,smtplib
conna = smtplib.SMTP("smtp.gmail.com",587)
conna.ehlo()
conna.starttls()
conna.login(email,password)
###
import sys

def emails_checker():
    deleting_list = [] # a list to store the emails that will be deleted later
    conn.select_folder("INBOX",readonly=False) #updating the inbox folder
    
    updated_uids = conn.search(["SINCE",formated_date]) #checking email list again
    
    updated_uids = [uid for uid in updated_uids if uid not in initial_UIDS] #selecting new emails
    
    

        
        
    if not updated_uids: #if no new emails
        print("No new emails")
        return
    for new_uid in updated_uids:
        raw_msg = conn.fetch([new_uid],["BODY[]","FLAGS"])   #fetching the message
        message = pyzmail.PyzMessage.factory(raw_msg[new_uid][b"BODY[]"])#parsing the message
        

        if not message.text_part: #if email has no txt part dont check It
            print("No text part found")
            continue
        email_content = message.text_part.get_payload().decode(message.text_part.charset)
        if key_word not in email_content: #if key word not found dont check it
            print("No key word found")
            continue
        message_source = message.get_address('from') #getting the email source
        #when keyword is found, and email has a txt part, then the work starts!
        split_email_content = email_content.split("\n")
        #first element should be the keyword
        #second element should be the command
        #third element should be an optional a link or Idk


        if "torrent" in split_email_content[1] :
            file_loc = os.path.join(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials", split_email_content[2].strip())

            sub_proc_obj = subprocess.Popen([ r"C:\Program Files\qBittorrent\qbittorrent.exe", "--sequential", "--no-splash", file_loc ])         
            
            sub_proc_obj.wait()   
            conna.sendmail(email,message_source[1],f"Subject: Command Executed\n\nDownloaded the torrent file\n{split_email_content[2]}")
            deleting_list.append(new_uid) # adding the email to be deleted
        else:
            conna.sendmail(email,message_source[1],f"Subject: Command Failed\n\nCommand not recognized") #sending the error message in case It fails
            deleting_list.append(new_uid) #another deletion
            
    print("deleting emails")
    conn.delete_messages(deleting_list)  #adding emails to be deleted
    conn.expunge() #the actual deleting of the emails
            
        
    
      
while True:
    
    time.sleep(5)
    
    emails_checker()
