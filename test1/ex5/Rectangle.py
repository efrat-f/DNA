from ex5.Shape import Shape


class Rectangle(Shape):
    def __init__(self, width, length):
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__length

    def calculate_perimeter(self):
        return (self.__width + self.__length) * 2
