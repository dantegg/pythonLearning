print(sorted([3,-2,2,-53,23,11]))


print(sorted([3,-2,-4,-56,23,11],key=abs))

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
    return str.lower(t[0])


result = sorted(L,key=by_name) #按照姓名字母顺序

print(result)

L2 = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]


def by_score(s):
    return s[1]

result2 = sorted(L2,key=by_score,reverse=True)  #按照分数从高到低

print(result2)
