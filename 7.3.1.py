import time


def decorator_time(old_funciton):
    def new_function(*args, **dict_arg):
        t1 = time.time()
        result = old_funciton(*arg, **dict_arg)
        t2 = time.time()
        print('time: ', t2 - t1)
        return result
    return new_function


def decorator_class(SomeClass):
    class NewClass(object):
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = SomeClass(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()

    return NewClass


@decorator_class
class Bird:
    def __init__(self, age):
        self.age = age

    def display(self):
        print('My age is', self.age)


if __name__ == '__main__':
    eagle_loard = Bird(5)
    for i in range(3):
        eagle_loard.display()