import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule # type: ignore
import time
from datetime import datetime

# Function to send email
def send_email(to_email, subject, body):

    from_email = 'nishanth.iipcmci@chavaraacademy.in'
    password = '1905@2003'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# List of dates in 'YYYY-MM-DD' format
dates = ['2024-06-08', '2024-06-15', '2024-06-09']

# Email details
to_email = 'nishanthdmello2003@gmail.com'
subject = 'Scheduled Email'
body = 'This is a scheduled email.'

# Function to schedule an email on a specific date
def schedule_email(date):
    schedule_date = datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.now().date()
    if schedule_date >= today_date:
        schedule.every().day.at("15:18").do(check_date_and_send_email, date).tag(date)

# Check if today is the scheduled date and send the email
def check_date_and_send_email(date):
    if datetime.now().strftime('%Y-%m-%d') == date:
        send_email(to_email, subject, body)
        schedule.clear(date)  # Clear the schedule once the email is sent

# Schedule emails for each date in the list
for date in dates:
    schedule_email(date)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)