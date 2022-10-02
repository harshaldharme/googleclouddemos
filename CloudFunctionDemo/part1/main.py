# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg = SendGridAPIClient('APIKEY')

def send_mail(data, context):
    message = Mail(
        from_email='from@email.com',
        to_emails='to@email.com',
        subject='Subjectline',
        html_content="Hello <strong>Harshal</strong>, <br/>The file which was uploaded to <strong>{}</strong> is <strong>{}</strong>.<br/>Download Link: {} <br/>Thank You..!".format(data['bucket'], data['name'], data['mediaLink'])
    )
    response = sg.send(message)