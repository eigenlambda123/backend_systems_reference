from app.tasks import celery_app

# This file just exposes `celery_app` so you can run:
# celery -A app.celery_worker.celery_app worker --loglevel=info
