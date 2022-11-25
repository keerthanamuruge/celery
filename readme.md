Celery with Django

install all requirements

<code>pip install -r requirements.txt</code>

start redis
<code> redis-server</code>

To check redis server has start

<code> redis-cli ping </code>

The response will be pong

To install celery and redis in single command
<code> pip install -U Celery[Redis] </code>

To restart redis server
<code>/etc/init.d/redis-server restart</code>
or stop/start it:

<code>/etc/init.d/redis-server stop
/etc/init.d/redis-server start</code>

Run celery
<code>celery -A mysite.celery worker --pool=prefork --concurrency=4  -l info

celery -A mysite.celery worker --pool=solo --concurrency=1 --loglevel=info
</code>