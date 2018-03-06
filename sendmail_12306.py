import smtplib

Sendmail = smtplib.SMTP_SSL('smtp.exmail.qq.com',465)

Sendmail.ehlo()

#Sendmail.starttls()

User = 'youremail'

Passwd = 'yourpassword'

Sendmail.login(User,Passwd)

To = 'receiveemail'

#message = input('Please input the message;')

message = """From: From Person <youremail>
To: To Persion <receviceemail>
Subject: Have tickets!

Now have some tickets,go to buy it!
"""
Sendmail.sendmail(User,To,message)

Sendmail.quit()
