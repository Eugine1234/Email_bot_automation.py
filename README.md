# Email_bot_automation.py
 How the Email Automation Bot Works
This script will serve as a basic email sender bot. Here's a breakdown of its functionality and the underlying principles:

SMTP Protocol (Sending Mail):

Email sending relies on the Simple Mail Transfer Protocol (SMTP). When you send an email, your email client (or our Python script) connects to an SMTP server provided by your email service (e.g., Gmail's SMTP server).
The SMTP server then handles the relaying of your email to the recipient's mail server.
smtplib Library:

Python's smtplib module simplifies interacting with SMTP servers. It allows us to establish a connection, authenticate (log in), and send the email.
email.mime.text Library:

Creating a properly formatted email message (with sender, recipient, subject, and body) can be complex due to MIME (Multipurpose Internet Mail Extensions) standards.
The email.mime.text module helps us construct email messages in a standardized way, ensuring they are correctly interpreted by mail clients.
Security and Authentication:

To send emails through a service like Gmail, you need to authenticate with your username (email address) and password.
Important: If you have 2-Factor Authentication (2FA) enabled on your Gmail account (which is highly recommended for security), you cannot use your regular Gmail password directly in scripts. Instead, you must generate an App Password from your Google Account settings. This is a unique, one-time password specifically for applications that don't support 2FA directly.
NEVER hardcode your actual email password or app password directly in your script for production use. For this example, I'll prompt for input, but in a real-world scenario, you'd use environment variables or a secure configuration management system.
SSL/TLS Encryption:

To secure the communication between your script and the SMTP server, we use SSL/TLS encryption. smtplib supports starttls() to upgrade a connection to a secure one.
Workflow of the Script:

Gather Information: The script prompts the user for the sender's email, password, recipient's email, subject, and message body.
Create Message Object: It constructs an MIMEMultipart (or MIMEText) object, setting the From, To, and Subject headers.
Connect to SMTP Server: It establishes a secure connection to the specified SMTP server (e.g., smtp.gmail.com on port 587).
Login: It authenticates using the provided email and password/app password.
Send Email: It sends the formatted email message using the authenticated connection.
Close Connection: The connection to the SMTP server is closed.
