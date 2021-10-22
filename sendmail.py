import smtplib

gmail_user = input("Enter Sender's User-mail : ")
gmail_password = input("Enter Sender's Password : ")
r1 = input("Enter reciever E-mail address : ")
sent_from = gmail_user
to = [r1]
subject = input("Enter subject : ")
body = input("Enter Body of your mail : ")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong….",ex)
