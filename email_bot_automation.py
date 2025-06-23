import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import getpass # For securely getting password input

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email using the provided sender, receiver, subject, and body.
    Assumes Gmail's SMTP server (smtp.gmail.com, port 587) for demonstration.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587 # Standard port for STARTTLS

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # Optional: message["Bcc"] = "bcc@example.com"
    # Optional: message["Cc"] = "cc@example.com"

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    try:
        # Create a default SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server
        print(f"Connecting to SMTP server: {smtp_server}:{smtp_port}...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Secure the connection with TLS
            server.starttls(context=context)
            print("TLS connection established.")

            # Login to the email account
            server.login(sender_email, sender_password)
            print("Logged in successfully.")

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("\nERROR: Authentication failed.")
        print("Please check your email address and password/App Password.")
        print("If using Gmail with 2FA, you NEED an 'App Password' from Google Account security settings.")
        print("Go to: Google Account -> Security -> How you sign in to Google -> App passwords.")
    except smtplib.SMTPConnectError as e:
        print(f"\nERROR: Could not connect to SMTP server. Check server address/port or internet connection: {e}")
    except smtplib.SMTPException as e:
        print(f"\nERROR: An SMTP error occurred: {e}")
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred: {e}")

def main():
    print("--- Python Email Automation Bot ---")
    print("This bot uses Gmail's SMTP server for sending emails.")
    print("If you have 2FA enabled on Gmail, you MUST use an 'App Password'.")
    print("Generate it at: myaccount.google.com/security -> App passwords.")
    
    sender_email = input("\nEnter your Gmail address: ").strip()
    # Use getpass for secure password input (doesn't echo to console)
    sender_password = getpass.getpass("Enter your Gmail password (or App Password for 2FA): ").strip()
    
    receiver_email = input("Enter the recipient's email address: ").strip()
    subject = input("Enter the email subject: ").strip()
    body = input("Enter the email body: ").\
        replace('\\n', '\n') # Allow user to type \n for new lines
    
    send_email(sender_email, sender_password, receiver_email, subject, body)

    print("\n--- Email Bot Finished ---")

if __name__ == "__main__":
    main()