#To ensure that Celery will start together with Django. we are importing the celery app
from .celery import app as celery_app

__all__ = ('celery_app',)