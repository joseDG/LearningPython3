class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


r = Rectangle(2, 5)
print(r.get_area())  # 10

c = Circle(5)
print(c.get_area())  # 78.5
