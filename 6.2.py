class Bird(object):
    feather = True

    def chirp(self):
        print("some sound")


class Chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def chirp(self):
        print("ji")

summer = Chicken(2)
# print("===> summer")
# print(summer.__dict__)
# print("===> chicken")
# print(Chicken.__dict__)
# print("===> bird")
# print(Bird.__dict__)
# print("===> object")
# print(object.__dict__)

class num(object):
    def __init__(self, value):
        self.value = value

    def get_neg(self):
        return -self.value

    def set_neg(self, value):
        self.value = -value

    def del_neg(self):
        print("value so deleted")
        del self.value

    neg = property(get_neg, set_neg, del_neg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg
