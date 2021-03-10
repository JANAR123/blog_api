from django.core.mail import send_mail
from django.conf import settings

def send_to_mail(email,code):
    link=settings.ALLOWED_HOSTS[0]+':8000/authe/confirm/'
    return send_mail('Blog',link+code,settings.EMAIL_FROM,[email,])