#Alert module. Sends emails and text messages

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__host_email_address = "NAS@localhost"


def send_text():
  print("Sending text")
  raise NotImplementedError


def send_email(address,subject,message):
  print("Sending Email")

  me = __host_email_address
  you = address;
  
  msg = MIMEMultipart('alternative')
  msg['Subject'] = subject
  text = message['plain']
  html = message['html']
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')

  msg.attach(part1)
  msg.attach(part2)

  s = smtplib.SMTP('localhost')

  s.sendmail(me,you,msg.as_string())
  s.quit()

