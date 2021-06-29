class Card:
    def __init__(self, type1, number):
        if type1 not in ["red", "blue", "green", "yellow"] or type(number) != int or number > 10 or number < 1:
            print("invalid type or number")
            return
        self.__type1 = type1
        self.__number = number

    def get_type(self):
        return self.__type1

    def set_type(self):
        return self.__type1

    def get_number(self):
        return self.__type1

    def set_number(self):
        return self.__type1

    def __str__(self) -> str:
        return "type: {}, number: {}".format(self.__type1, self.__number)


