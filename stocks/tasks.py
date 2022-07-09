from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .email import send_feedback_email, attachment_send
from celery.utils.log import get_task_logger

loger = get_task_logger(__name__)

@shared_task
def debug_task():
    print('This is a debug task')
    return 'This is a debug task'

@shared_task(name='send_feedback_email_task')
def send_feedback_email_task(name, email, feedback):
    loger.info('Sending feedback email',name, email, feedback)
    print('Sending feedback email :',name, email, feedback)

    return send_feedback_email(name, email, feedback)


@shared_task(name='attchment_send_task')
def attachment_send_task(request, file_name):
    loger.info('Sending attachment email : ',request.user)
    print('Sending attachment email')

    return attachment_send(request, file_name)
