import smtplib
import ssl
import os


# Function to send an email
def send_email(message):
    """
    Sends an email using SMTP_SSL.
    Args:
        message (str): The content of the email to be sent.
    """
    # SMTP server details
    host = "smtp.gmail.com"  # Gmail's SMTP server
    port = 465  # SSL port for SMTP
    username = os.getenv("FORM_EMAIL")  # Sender's email address
    password = os.getenv("PASSWORD")  # Email account password
    receiver = os.getenv("FORM_EMAIL")  # Recipient's email address

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            # Attempt to log in to the server
            server.login(username, password)

            # Send the email
            server.sendmail(username, receiver, message)
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        # Handle authentication errors
        print("Error: Authentication failed. Check your username and password.")

    except smtplib.SMTPException as e:
        # Handle other SMTP-related errors
        print(f"SMTP error occurred: {e}")

    except Exception as e:
        # Handle any other unforeseen errors
        print(f"An error occurred: {e}")
