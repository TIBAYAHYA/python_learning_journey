""" planned on using, ezgmail library, but then remembered that Im a coder and I love suffering, plus I dont think Its gonna be better, the thing is
demanding an API while the other library only requires an app password, Im gonna stick to smtplib and imapclient
"""
import smtplib
#imaplib._MAXLINE = 10000000 # change python default size limit
smtp_obj = smtplib.SMTP("smtp.gmail.com","587")
smtp_obj.starttls()
smtp_obj.login("my_email","password")
smtp_obj.sendmail("my_email","target_email","Subject: hey bro.\nWhat is up, can you please do the stuff.Sincerement, him")
smtp_obj.quit()