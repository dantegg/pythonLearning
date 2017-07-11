# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100！')
#         self._score = value


# s = Student()
# s.score = 60
# print(s.score)
# s.score = 99
# print(s.score)
# s.score = 999999
# print(s.score)


class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth    


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def resolution(self):
        return self.width * self.height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)