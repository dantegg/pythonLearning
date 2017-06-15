# from threading import Thread
import multiprocessing

x = 5

#
# def double():
#     global x
#     x = x * 2
#
#
# def plus_ten():
#     global x
#     x = x + 10
#
# thread1 = Thread(target=double)
# thread2 = Thread(target=plus_ten)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# print(x)


def proc1():
    return 999999**9999


def proc2():
    return 888888**8888
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=proc1)
    p2 = multiprocessing.Process(target=proc2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()