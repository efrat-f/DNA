import math

from ex5.Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__radius * self.__radius * math.pi

    def calculate_perimeter(self):
        return self.__radius * 2 * math.pi
