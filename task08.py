class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



rect1 = Rectangle(5, 10)
print("1-rectangle yuzi:", rect1.area())

rect2 = Rectangle(7, 3)
print("2-rectangle yuzi:", rect2.area())