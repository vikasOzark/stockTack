from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import os

def send_feedback_email(name, email, feedback):
    context = {
        'name': name,
        'email': email,
        'feedback': feedback
    }
    subject = 'Thank you for your feedback'
    email_body = render_to_string('email_message.txt', context)
    email_send = EmailMessage(subject, email_body, settings.DEFAULT_FROM_EMAIL, [email,])
    print(type(email_send))
    # file_path = os.path.abspath('excel-file/stock-data7.xlsx')
    # email_send.attach_file(file_path)
    return email_send.send(fail_silently=False) 



def attachment_send(request, file_name):
    context = {
       'username': request.user,
    }
    subject = 'Thank you for using our service '
    body = render_to_string('attachment.txt', context)
    email_send = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL,[request.user.email,])
    file_name = str(file_name)
    print('type of file : ', type(file_name),' : ', file_name)
    full_path = os.path.abspath(file_name)
    email_send.attach_file(full_path)

    return email_send.send(fail_silently=False)