import os
from dotenv import load_dotenv # type: ignore
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv() 

sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")
subject = "Hello from Python"
body = "Hello, this is a test email from Python."

# Create a message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Create SMTP session
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        # Start TLS for security
        s.starttls()
        # Authentication
        s.login(sender_email, sender_password)
        # Send the email
        s.send_message(message)
    print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", str(e))

