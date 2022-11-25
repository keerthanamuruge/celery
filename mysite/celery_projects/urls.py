from django.urls import path
from .views import index, test_binary_search, test_celery

urlpatterns = [
    path('', index, name='index'),
    path('c/', test_binary_search, name='test_binary_search'),
    path('celery/', test_celery, name='test_celery')
]