import schedule # type: ignore
from datetime import datetime
import time
import smtplib
import os
from dotenv import load_dotenv # type: ignore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st # type: ignore


def send_email(name):

    sender_email = "nishanth.iipcmci@chavaraacademy.in"
    sender_password = "1905@2003"
    recipient_email = "nishanthdmello2003@gmail.com"
    subject = name + "'s Birthday Today"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    body = "It is " + name + "'s birthday today."
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, sender_password)
            s.send_message(message)

    except Exception as e:
        print("Failed to send email:", str(e))


st.write("welcome to birthday teller")

load_dotenv() 

dates = [
    "2024-06-08",
    "2024-06-08",
    "2024-06-08",
    "2024-06-08"
]

names = [
    "Nishanth D'Mello",
    "N Digvijay",
    "Monish D",
    "Nihal T M"
]

def schedule_email_on_date(date, name):
    def job():
        if datetime.now().strftime("%Y-%m-%d") == date:
            send_email(name)

    schedule.every().day.at("20:04").do(job).tag(date)

for date, name in zip(dates, names):
    schedule_email_on_date(date, name)

def job_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

job_scheduler()