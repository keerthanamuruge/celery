from __future__ import absolute_import

from celery import Celery

app = Celery('mymodule',
             broker='amqp://',
             backend='amqp://',
             include=['mymodule.tasks'])

if __name__ == '__main__':
    app.start()