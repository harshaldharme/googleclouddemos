# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from json import load as json_load
from wand.image import Image
from google.cloud import storage

sg = SendGridAPIClient('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')

with open('config.json') as json_data_file:
    cfg = json_load(json_data_file)

client = storage.Client()

def process_send_email(data, context):
    # Get the image from GCS
    bucket = client.get_bucket(data['bucket'])
    blob = bucket.get_blob(data['name'])
    imagedata = blob.download_as_string()

    # Create a new image object and resample it
    newimage = Image(blob=imagedata)
    newimage.sample(300,300)

    # Upload the resampled file to the thumbnails bucket
    bucket = client.get_bucket(cfg['THUMBNAIL_BUCKET'])
    newblob = bucket.blob('thumbnail-'+data['name'])
    newblob.upload_from_string(newimage.make_blob())

    message = Mail(
        from_email='edurekagcpbatch18062022@gmail.com',
        to_emails='hvdharme@gmail.com',
        subject='LearnWithHarshal - File conversion',
        html_content="Hello <strong>Harshal</strong>, <br/>The file which was uploaded to <strong>{}</strong> is <strong>{}</strong>.<br/>Original File: {} <br/>Thumbnail generated and uploaded at: {} as: {}<br/>Thank You..!".format(data['bucket'], data['name'], data['mediaLink'], cfg['THUMBNAIL_BUCKET'], 'thumbnail-'+data['name'])
    )
    response = sg.send(message)