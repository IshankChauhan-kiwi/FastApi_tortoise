from fastapi import UploadFile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader

from utils.settings import settings


def send_email(receiver, subject, body, attachment: UploadFile = None):
    msg = MIMEMultipart()
    msg['From'] = settings.FROM_EMAIL
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file, if provided
    if attachment is not None:
        attachment_content = attachment.file.read()
        attachment_name = attachment.filename
        attachment_type = attachment.content_type
        attachment = MIMEApplication(attachment_content, _subtype=attachment_type)
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        msg.attach(attachment)

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.FROM_EMAIL, receiver, msg.as_string())


def send_email_with_template(receiver, subject, template_name, context, attachment: UploadFile = None):
    # Load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    # Render the template with the context
    body = template.render(context)

    msg = MIMEMultipart()
    msg['From'] = settings.FROM_EMAIL
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Attach the file, if provided
    if attachment is not None:
        attachment_content = attachment.file.read()
        attachment_name = attachment.filename
        attachment_type = attachment.content_type
        attachment = MIMEApplication(attachment_content, _subtype=attachment_type)
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        msg.attach(attachment)

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(settings.FROM_EMAIL, receiver, msg.as_string())
