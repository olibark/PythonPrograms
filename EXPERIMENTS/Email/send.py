import smtplib
from email.mime.text import MIMEText

# Email content
msg = MIMEText("This is the email body.")
msg["Subject"] = "Test Email"
msg["From"] = "your_email@example.com"
msg["To"] = "recipient@example.com"

# SMTP server details
smtp_server = "smtp.example.com"
smtp_port = 587
username = "your_email@example.com"
password = "your_password"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Secure the connection
    server.login(username, password)
    server.send_message(msg)

print("Email sent!")