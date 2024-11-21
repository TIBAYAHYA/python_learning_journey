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
start_now = datetime.datetime.now()  #the now time
formated_date = start_now.strftime("%d-%b-%Y")   #correct format that gets accepted as a second argument of conn.search()
key_word = "Magito_the_idiot"        #keyword to be checked in each mail





initial_UIDS = conn.search(["SINCE",formated_date])  #searching for emails sent "today" according to time shot




import subprocess,os
cwd = os.getcwd()
import time,pyzmail
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
        #when keyword is found, and email has a txt part, then the work starts!
        split_email_content = email_content.split("\n")
        #first element should be the keyword
        #second element should be the command
        #third element should be an optional a link or Idk
        if split_email_content[1] == "torrent":
            
            os.chdir(r"C:\Users\maroc\OneDrive\Desktop\coding journey\automate_online-materials")
            sub_proc_obj = subprocess.Popen("C:\\Program Files (x86)\\qBittorrent\\qbittorrent.exe",split_email_content[2])
            sub_proc_obj.wait()   
            deleting_list.append(new_uid)
                     
            #todo, 
            # add an actual downloable torrent file, to test the program
            #delete the email after the command is executed
            # add a confirmation email that signals that the progress worked or/ finished
            #maybe add more commands
        

                
            
    
    
    
    
      
while True:
    
    time.sleep(5)
    
    emails_checker()
