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


class Editor:
    def __init__(self):
        self.rect = None
        self.circle = None

    def create_rectangle(self, width, height):
        self.rect = Rectangle(width, height)

    def create_circle(self, radius):
        self.circle = Circle(radius)

    def change_rectangle(self, factor):
        if self.rect == None:  # we should use is None (soon)
            return

        width, height = self.rect.width + factor, self.rect.height + factor
        self.create_rectangle(width, height)

    def change_circle(self, factor):
        if self.circle == None:  # we should use is None (soon)
            return

        self.create_circle(self.circle.radius + factor)

    def change(self, factor):
        self.change_rectangle(factor)
        self.change_circle(factor)

    def print(self):
        if self.rect != None:
            print("Rectangle area", self.rect.get_area())

        if self.circle != None:
            print("Circle area", self.circle.get_area())


editor = Editor()
editor.create_rectangle(3, 5)
editor.print()
# Rectangle area 15
editor.create_circle(5)
editor.change(2)
editor.print()
# Rectangle area 35
# Circle area 153.86
