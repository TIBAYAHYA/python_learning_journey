"""this program is supposed to assign random chores to a list of people and send them an email containing their assigned chore,
   the program should not assign the same chore twice in a row
"""



import random,time
people_mails_dict = {"Abdul":"abdul@gmail.com", "Bilal":"bilal@gmail.com", "Cem":"cem@gmail.com", "Dilan":"dilan@gmail.com"}


#shore assigning function
def assign_chores():
   global assignement_dict
   
   chores = ["dishes", "bathroom", "vacuum", "walk dog"]
   
   random.shuffle(chores)  # shuffle the chores
   assignement_dict = {}
   for person in list(people_mails_dict.keys()):  # iterate over people in the form of a list
      assignement_dict[person] = chores.pop()   # remouve
   data_storing()
      
      



#data storing in the form of a json file to permanently keep track of previous records
def data_storing():
   import json
   with open("assignements.json","r") as json_file:
      json_content = json.load(json_file)    #load the content of json file as the old assignement


   for key,value in assignement_dict.items():
      if json_content.get(key) == value:   #keep shuffling until we find the correct version of assignement
         assign_chores()
   with open("assignements.json","w") as json_file:
      json.dump(assignement_dict,json_file)        #load correct assignement into json file
      
   email_sending()
   
   
### smtllibing stuff
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
email = input("enter your email: ")
password = input("enter your password: ")
conn.ehlo()
conn.starttls()
conn.login(email, password)




### email sending function
def email_sending():
   for key,value in assignement_dict.items():   #iterate over the assignement dictionary
      conn.sendmail(email,people_mails_dict[key],f"Subject: Your chore for this week is {value} \n\n")
   conn.quit()
   print("Emails Sent!")
   time.sleep(60)  
   weekly_timing()
      
      


import datetime

def weekly_timing():
   while True:
      now = datetime.datetime.now()    #constantly updating now time
      if now.weekday()== 6 and now.hour == 15 and now.minute ==(30):  
         #part of the code that constantly checks if it is equal to set date
         print("weekly timed")
         assign_chores()
         time.sleep(60)    
      else:
         print("not yet!")
         time.sleep(60)
         
weekly_timing()