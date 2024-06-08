import time
import datetime
import smtplib
import os
from dotenv import load_dotenv # type: ignore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M:%S & %d-%m-%Y ")

def send_email(recipient, subject, body):

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("PASSWORD")
    subject = formatted_time

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, sender_password)
            s.send_message(message)
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email:", str(e))


load_dotenv() 


# List of dates (in string format for this example)
dates_list = [
    "2024-06-08 16:08:00",
    "2024-06-11 10:30:00",
    "2024-06-12 14:00:00"
]

# Convert string dates to datetime objects
dates = [datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S") for date_str in dates_list]

# Recipient email, subject, and body of the email
recipient_email = os.getenv("RECIPIENT_EMAIL")
email_subject = "Scheduled Email"
email_body = "This is a scheduled email."

# Main loop to check dates and send emails
while dates:
    now = datetime.datetime.now()
    for date in dates:
        if now >= date:
            send_email(recipient_email, email_subject, email_body)
            dates.remove(date)  # Remove the date after sending the email
    time.sleep(60)  # Sleep for 1 minute before checking again
