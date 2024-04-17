import math

class Geometry_Area:
    def valid_area(self, num1, num2):
        self.num1 = num1
        self.num2 = num2



class Rectangle(Geometry_Area):
    def __init__(self, num1, num2):
        self.area = num1 * num2

class Triangle(Geometry_Area):
    def __init__(self, num1, num2):
        # self.area = math.sqrt((num1 * num1) + (num2 * num2))
        self.area = (0.5 * num1 * num2)
        
    # def valid_area(self):
    #     if self.area > 0:
    #         return self.area
    #     else: 
    #         raise ValueError(False)

class Square(Geometry_Area):
    def __init__(self, num1):
        self.area = num1 * num1




# print(issubclass(Rectangle, Geometry_Area))

tri_1 = Triangle(4, 10)

print(tri_1.area)