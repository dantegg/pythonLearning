def line_conf():
    def line(x):
        return 2 * x + 1
    return line

my_line = line_conf()
print(my_line(5))


def line_conf2():
    b = 15

    def line(x):
        return 2 * x + b
    b = 5
    return line

if __name__ == "__main__":
    my_line = line_conf2()
    print(my_line.__closure__)
    print(my_line.__closure__[0].cell_contents)


def line_conf3(a, b):
    def line(x):
        return a * x + b

    return line

line1 = line_conf3(1, 1)
line2 = line_conf3(4, 5)
line3 = line_conf3(5, 10)
line4 = line_conf3(-2, -6)


def curve_closure(a, b, c):
    def curve(x):
        return a * x ** 2 + b * x + c
    return curve
curve1 = curve_closure(1, 2, 1)