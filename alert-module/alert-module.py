#Alert module. Sends emails and text messages

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
  _send_text()
  _send_email()


def _send_text():
  print("Sending text")
  raise NotImplementedError


def _send_email():
  print("Sending email")
  raise NotImplementedError


if __name__ == "__main__":
  main()


