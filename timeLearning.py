# import time
# import datetime
#
# # print("start")
# # time.sleep(10)
# # print("wake up")
#
# start = time.clock()
# for i in range(100000):
#     print(i**2)
#
# end = time.clock()
# print(end - start)
#
# t = datetime.datetime(2017, 6, 5, 21, 30)
# print(t)
#
# next_t = datetime.datetime(2017, 6, 5, 21, 30)
#
# delta1 = datetime.timedelta(seconds=600)
# delta2 = datetime.timedelta(weeks=3)
#
# print(t+delta1)
# print(t+delta2)
# print(next_t-delta2)

from datetime import datetime

# str = "output-1997-12-23-030000.txt"
#
# format = "output-%Y-%m-%d-%H%M%S.txt"
#
# t = datetime.strptime(str, format)
#
# print("time is")
# print(t)


format2 = "%Y-%m-%d %H:%M"
test_time = datetime(2017, 6, 5, 23, 39)
print(test_time.strftime(format2))
