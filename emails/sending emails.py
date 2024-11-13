""" simple code that send email to a destination email using smtplib module
    had to add input for email and password to not expose my/user email and password
"""
import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
email = input("enter your email: ")
password = input("enter your password: ")
#user_email = input("what is your email?:\n")
#user_password = input("what is your password?:\n")
conn.ehlo()
conn.starttls()
conn.login(email, password)
destination = input("enter your destination email: ")
subject = input("enter your subject: ")
message = input("enter your message: ")
conn.sendmail(email,destination,f"Subject: {subject} \n\n{message}")
conn.quit()