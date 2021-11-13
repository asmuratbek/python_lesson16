from main import Shape, Square, Rectangle, Circle

sq1 = Square(12)
sq2 = Square(4)
# print(sq1.get_sq_area())
# print(sq2.get_sq_area())

rt1 = Rectangle(3, 4)
rt2 = Rectangle(4, 6)
# print(rt1.get_rt_area())
# print(rt2.get_rt_area())
c1 = Circle(12)
c2 = Circle(4)
shape = Shape()

figures = [sq1, sq2, rt1, rt2, c1, c2]

for figure in figures:
    print(figure, figure.get_area())