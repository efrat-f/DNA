import math
from ex5.Shape import Shape


class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return math.sqrt(math.pow(self.__side, 2) + math.pow(self.__side/2, 2)) * self.__side

    def calculate_perimeter(self):
        return self.__side * 3
