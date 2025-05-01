
from celery import Celery

celery = Celery("worker", broker="redis://redis:6379/0")
