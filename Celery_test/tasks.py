from __future__ import absolute_import
from celery import Celery
# from Celery_test.sett import app
app = Celery('tasks',
             backend='mongodb://127.0.0.1:27017//',
             broker='mongodb://127.0.0.1:27017//',
             )
class Celery_task:

    # to start server :- C:\Python27\Scripts\celery -A tasks worker --loglevel=info
    # in virtual env :- celery -A tasks worker --loglevel=info

    @app.task
    def add(self, x, y):
        return x + y

    @app.task
    def sub(self, x, y):
        return x - y

    @app.task
    def mul(self, x, y):
        return x * y

    @app.task
    def div(self, x, y):
        return x / y

    # add.delay(5, 10)
    # mul.delay(5, 10)

if __name__ == '__main__':
    c = Celery_task()

    c.add.delay(0, 5, 10)
    c.mul.delay(0, 5, 10)
    c.div.delay(0, 15, 5)