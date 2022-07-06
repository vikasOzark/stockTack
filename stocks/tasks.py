from __future__ import absolute_import, unicode_literals
from celery import shared_task
import celery

@shared_task
def debug_task():
    print('This is a debug task')
    return 'This is a debug task'

@task(name='send_feedback_task')
