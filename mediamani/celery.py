"""
Purpose of this file is to define celery instance so we can use celery

"""


from __future__ import absolute_import # https://stackoverflow.com/questions/33743880/what-does-from-future-import-absolute-import-actually-do
import os
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediamani.settings')

app = Celery('mediamani'
            )

# app.control.revoke(
#     [
#     'd5551335-ac1e-4823-94fd-aa8a20ab3d20',
#     '752e685f-a1ef-4a87-9a4e-96b693f2f622',
#     'db5fc5ae-1c5b-4394-a81e-353cca216ac7',
#     ]
# )

# lst = [
#     'd5551335-ac1e-4823-94fd-aa8a20ab3d20',
#     '752e685f-a1ef-4a87-9a4e-96b693f2f622',
#     'db5fc5ae-1c5b-4394-a81e-353cca216ac7',
#     ]
# for i in lst:
#     app.control.revoke(i, terminate=True)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

# SO WE ARE SAYING IT THAT IF ANY HAVE CONFIGURED ANYTHING, LOOK AT SETTING AND 
# NAMESPACE: EVERY CELERY CONFIGURATION SHOULD HAVE PREFIX = 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# TRY TO NAME YOUR TASKS FILE AS tasks.py inside every app folder
app.autodiscover_tasks()


# what is @app
# what is @app.task
"""
@app.task is used to create task or convert function into celery task
https://stackoverflow.com/questions/54506515/difference-between-different-ways-to-create-celery-task
there are different ways


"""


# what is bind =True
# effect of bind = False
# A task being bound means the first argument to the task will always be the task instance (self)
# so by using bind = True, we can get it's id
# https://stackoverflow.com/questions/54899320/what-is-the-meaning-of-bind-true-keyword-in-celery
@app.task(bind=True)
def debug_task(self):
    pass