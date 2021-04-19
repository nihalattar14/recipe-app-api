# import smtplib, ssl
#
# smtp_server = "smtp.greenlightcorp.com"
# print("1")
# port = 125  # For starttls
# sender_email = "No-reply@greenlightcorp.com"
# password = "Green123$"
# receiver_email = "nihalattar14@gmail.com"
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# print(message)
# try:
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)
# except Exception as e:
#     print(e)
# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL


login, password = 'No-reply@greenlightcorp.com', getpass('Green123$')
recipients = ["nihalattar14@gmail.com"]

# create message
msg = MIMEText('message body…', 'plain', 'utf-8')
msg['Subject'] = Header('subject…', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients)

# send it via gmail
s = SMTP_SSL('smtp.192.168.2.19.com', 125)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], recipients, msg.as_string())
finally:
    s.quit()
