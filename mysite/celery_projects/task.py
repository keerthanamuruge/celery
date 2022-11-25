import os

from celery import shared_task
from threading import Thread, current_thread
from multiprocessing import Process, current_process


@shared_task()
def test_cpu_bound_task():
    n= 200000000
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} \
        ---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} \
        ---> Finished counting...")
    return "Completed"


@shared_task()
def test_schedule():
    for i in "hello world":
        print(i)


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1