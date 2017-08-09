import itertools

naturalNumbers = itertools.count(1)
ns = itertools.takewhile(lambda x : x <= 10, naturalNumbers)
print(list(ns))

for c in itertools.chain('ABC','XYZ'):
    print(c)