class Shape:
    def __init__(self):
        self.__name = 'Square '

    def get_area(self):
        return 'Hello shape '

    def __str__(self):
        return self.__name + str(self.get_area())


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.__name = 'Square '

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return self.__name + str(self.get_area())

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.__name = 'Rectangle '

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return self.__name + str(self.get_area())

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
        self.__name = 'Circle '

    def get_area(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return self.__name + str(self.get_area())

