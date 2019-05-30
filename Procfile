web: gunicorn mystore.wsgi
worker: celery worker -A mystore  -l info --autoscale=1,0