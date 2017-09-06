import time
# 利用sched方法来执行定时任务
import sched

def run_Task():
    print('hahaha')

schedule = sched.scheduler(time.time, time.sleep)

def printTime(string1, float1):
    print("now is ", time.time(), "| output = ", string1, float1)

print('===========',time.time(),'==========')
schedule.enter(2,0, printTime, ("test1", time.time()))
schedule.enter(2,0, printTime, ("test1", time.time()))
schedule.enter(3,0, printTime, ("test1", time.time()))
schedule.enter(4,0, printTime, ("test1", time.time()))
schedule.run()
print('===========',time.time(),'==========')


