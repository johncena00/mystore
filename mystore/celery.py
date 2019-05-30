from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mystore.settings')

app = Celery(
    'mystore',
    broker=os.environ.get('CLOUDAMQP_URL'),
    broker_pool_limit=1,
    broker_heartbeat=None,
    broker_connection_timeout=30,
    result_backend=None,
    event_queue_expires=60,
    worker_prefetch_multiplier=1,
    worker_concurrency=1,
)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))