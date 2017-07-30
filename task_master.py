import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

