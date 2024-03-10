from django.core.mail import send_mail
from django.conf import settings
import requests

from celery import shared_task


@shared_task
def send_email_task(email_to):
    subject = 'Регистрация'
    message = 'Вы успешно зарегестрировались!'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email_to])    
   
