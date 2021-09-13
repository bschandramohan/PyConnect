import smtplib

EMAIL_ID = "pythonsmtptry@gmail.com"
PASSWORD = "python1234()"

# port = 465  # For SSL
# # Create a secure SSL context
# context = ssl.create_default_context()

print("Sending communication - 1")
with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context) as connection:
    print("Sending communication - 2")
    # connection.starttls()
    connection.login(EMAIL_ID, PASSWORD)
    connection.sendmail(EMAIL_ID,
                        EMAIL_ID,
                        "Subject:From Python Lib\n\nThis is Cool!"
                        )
    print("Email sent")
print("End Program")
