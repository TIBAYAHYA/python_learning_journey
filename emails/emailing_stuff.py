import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
#user_email = input("what is your email?:\n")
#user_password = input("what is your password?:\n")
conn.ehlo()
conn.starttls()
conn.login("yahyatiba12@gmail.com",)
