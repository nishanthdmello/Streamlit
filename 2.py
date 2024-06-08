import smtplib
import os
from dotenv import load_dotenv # type: ignore
import schedule # type: ignore
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(x):

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("PASSWORD")
    # recipient_email = os.getenv("RECIPIENT_EMAIL")
    recipient_email = x[0]
    subject = "Hello from Python"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(x[1], 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, sender_password)
            s.send_message(message)
        print("Email sent successfully!")

    except Exception as e:
        print("Failed to send email:", str(e))


load_dotenv() 

times = ["13:18", "13:20", "15:35"]
strings = ["Good morning!", "Lunch time!", "Good afternoon!"]

# for time_str, email_body in zip(times, strings):
#     schedule.every().day.at(time_str).do(send_email, [os.getenv("RECIPIENT_EMAIL"), email_body])

for time_str, email_body in zip(times, strings):
    schedule.every().day.at(time_str).do(send_email, [os.getenv("RECIPIENT_EMAIL"), time_str])

while True:
    schedule.run_pending()
    time.sleep(1)