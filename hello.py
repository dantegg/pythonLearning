#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

print(u'中文你好')

print('''line1
line2
line3
''')

print('Hi,%s,you have %d' % ('dantegg', 10000))


age = 3

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

height = input('your height(m)')
weight = input('your weight(kg):')

weight = float(weight)

height = float(height)


bmi = weight/(height*height)

print('your bmi is %f' % (bmi))

if bmi > 32:
    print ('严重肥胖')
elif bmi <= 32 and bmi >= 28:
    print ('肥胖')
elif bmi < 28 and bmi >= 25:
    print ('过重')
elif bmi < 25 and bmi >= 18.5:
    print ('正常')
elif bmi < 18.5:
    print ('过轻')
else:
    print ('???')



