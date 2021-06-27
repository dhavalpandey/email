import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import os

#Enviorment Variables
from dotenv import load_dotenv

load_dotenv()

OUTLOOK_EMAIL = os.getenv('OUTLOOK_EMAIL')
OUTLOOK_PASSWORD = os.getenv('OUTLOOK_PASSWORD')
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

#Terminal colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Sending email with GMAIL
def send_mail_gmail(email_recipient, email_subject, email_content):
    msg = EmailMessage()
    msg['Subject'] = email_subject
    msg['From'] = GMAIL_EMAIL
    msg['To'] = email_recipient

#Write your email in HTML here
    msg.add_alternative(f"""\
    {email_content}
    """, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"{bcolors.OKGREEN}Email sent successfully.{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}There was an error sending your email.{bcolors.ENDC}")

#Sending email with OUTLOOK
def send_mail_outlook(email_recipient, email_subject, email_content):

    msg = MIMEMultipart()
    msg['From'] = OUTLOOK_EMAIL
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(f"""\
    {email_content}
    """, 'html'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(OUTLOOK_EMAIL, OUTLOOK_PASSWORD)
        text = msg.as_string()
        server.sendmail(OUTLOOK_EMAIL, email_recipient, text)
        print(f"{bcolors.OKGREEN}Email sent successfully.{bcolors.ENDC}")
        server.quit()
    except:
        print(f"{bcolors.FAIL}There was an error sending your email.{bcolors.ENDC}")
    return True

def ask_instructions():
    send_to = input(f"{bcolors.BOLD}Recipient's email address: {bcolors.ENDC}")
    subject = input(f"{bcolors.BOLD}Subject of the email: {bcolors.ENDC}")
    html_file = input(f"{bcolors.BOLD}HTML file with email content (e.g. test.html): {bcolors.ENDC}")

    with open(html_file, "r", encoding='utf-8') as f:
        content = f.read()

    instruction = input("Do you want to send your email by Outlook? (y/n) \n")

    if instruction == "y":
        send_mail_outlook(send_to, subject, content)
    else:
        send_mail_gmail(send_to, subject, content)

ask_instructions()