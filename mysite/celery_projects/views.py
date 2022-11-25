from django.http import HttpResponse
from .task import test_cpu_bound_task


def index(request):
    test_cpu_bound_task()
    return HttpResponse("Hello, world. You're at the polls index.")


def test_binary_search(request):
    test_cpu_bound_task.delay()
    return HttpResponse("Blablablablablablablablablablablablablablablablabl")

def test_celery(request):
    test_cpu_bound_task.delay()
    return HttpResponse("Hello, world. Worked in celery")
