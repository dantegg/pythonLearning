def lazy_sum(*args):
    def sum_closure():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum_closure

f = lazy_sum(1, 3, 5, 7, 9)

print(f())


def count():
    def ft(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(ft(i))
    return fs

f1, f2, f3 = count()

print(f1())

print(f2())

print(f3())
