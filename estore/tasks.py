from __future__ import absolute_import, unicode_literals

import logging

from celery import shared_task
from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail_delay(*args, **kwargs):
    logging.warning('Send Mail Processing...')
    return django_send_mail(*args, **kwargs)


def send_mail(*args, **kwargs):
    logging.warning('Send Mail Pushed...')
    return send_mail_delay.delay(*args, **kwargs)