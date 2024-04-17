import math

class Geometry_Area:
    def valid_area(self):
        self.area = 0

    def valid_area(self):
            if self.area < 0:
                raise ValueError(False)

class Rectangle(Geometry_Area):
    def __init__(self, num1, num2):
        self.area = num1 * num2

class Triangle(Geometry_Area):
    def __init__(self, num1, num2):
        # self.area = math.sqrt((num1 * num1) + (num2 * num2))
        self.area = (0.5 * num1 * num2)

class Square(Geometry_Area):
    def __init__(self, num1):
        self.area = num1 * num1
