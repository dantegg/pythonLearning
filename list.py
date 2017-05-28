

temp = [1, 2, 3, 4, 5]


print(temp[0:3])

print(list(range(10)))


for i,value in enumerate(['A', 'B', 'C']):
    print(i,value)


temp2 = [x*x for x in range(1, 11) if x % 2 == 0]

print(temp2)

# import os

# print([d for d in os.listdir('.')])


L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s,str)]

# L2 = [item.lower() if isinstance(item, str) else item for item in L1]

print(L2)
