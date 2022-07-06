from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def senf_feedback_email(name, email, feedback):
    context = {
        'name': name,
        'email': email,
        'feedback': feedback
    }
    subject = 'Thank you for your feedback'
    email_body = render_to_string('email_message.txt', context)
    eamil = EmailMessage(subject, email_body, settings.DEFAULT_FROM_EMAIL, [email,])