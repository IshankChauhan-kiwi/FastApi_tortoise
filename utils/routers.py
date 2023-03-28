from fastapi import APIRouter, UploadFile, File
from utils.send_mail import send_email, send_email_with_template


router = APIRouter()


@router.post('/mail')
async def mail(receiver: str, subject: str, body: str, attachment: UploadFile = File(default=None)):
    send_email(
        receiver=receiver,
        subject=subject,
        body=body,
        attachment=attachment
    )
    return {"message": "mail sent successfully"}


@router.post('/mail_template')
async def mail_template(receiver, subject, template_name, attachment: UploadFile = File(default=None)):
    context = {"abc": "abc"}
    send_email_with_template(
        receiver=receiver,
        subject=subject,
        template_name=template_name,
        context=context,
        attachment=attachment
    )
    return {"message": "mail sent successfully"}
