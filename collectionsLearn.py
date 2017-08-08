from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print('q', q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


d = dict([('a',1),('c',3),('b',2)])
print(d)
od = OrderedDict([('a',1),('c',3),('b',2)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)