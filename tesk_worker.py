# task worker py

import time, sys, queue from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManager 只从网络上获取Queue, 所以注册时只提供名字