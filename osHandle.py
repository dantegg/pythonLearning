import os
print(os.name)
# windows 不提供uname
# print(os.uname()) 

# print(os.environ)

print(os.path.abspath('.'))