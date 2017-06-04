import time

# print("start")
# time.sleep(10)
# print("wake up")

start = time.clock()
for i in range(100000):
    print(i**2)

end = time.clock()
print(end - start)