# Alert module. Sends emails and text messages

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__host_email_address = "NAS@raspberrypi"

__REGION = "Canada"

"""
def send_text(numstring,message):
   params = urllib.urlencode({'number': numstring, 'message': message})
   headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
   conn = httplib.HTTPConnection("textbelt.com:80")
   if __REGION == "Canada":
     conn.request("POST", "/canada", params, headers)
   else:
     conn.request("POST", "/text", params, headers)
   response = conn.getresponse()
   return response.status, response.reason
"""


def send_email(address, subject, message):
    me = __host_email_address
    you = address

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    text = message['plain']
    html = message['html']
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('nutrition.automation@gmail.com', 'nutrition_automation')
    # s = smtplib.SMTP('127.0.0.1')
    s.sendmail(me, you, msg.as_string())
    s.close()