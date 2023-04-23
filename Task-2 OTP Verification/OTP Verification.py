import os
import math
import random
import smtplib

digit="123456789"
OTP=""
for i in range(6):
    OTP=OTP+digit[math.floor(random.random()==10)]
msg=OTP
s=smtplib.SMTP_SSL("smtp.gmail.com",465)
Email_id=input("Enter your e-mail id:")
s.login(Email_id,"dmls raiu nnsr zbeb")
send_to=input("Send To:")
s.sendmail(Email_id,send_to,msg)
d = input("Enter 6 digit OTP>>:")
if(d == OTP):
    print("OTP Verified")
else:
    print("Please check your OTP again")
