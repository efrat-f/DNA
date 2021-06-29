import json

from ex2 import check_validity, random_password
from ex3.Deck import Deck
from ex4 import my_reduce
from ex5.Circle import Circle
from ex5.EquilateralTriangle import EquilateralTriangle
from ex5.Rectangle import Rectangle
from ex5.Square import Square
from ex1 import merge


def test_ex1():
    merge("./resource/file_A", ".\\resource\\file_B", "./resource/combination.json", [1, 2, 3, 0])
    with open("./resource/combination.json", "r") as combine_file:
        assert json.load(combine_file) == {
            "Line 1": [
                "dsga",
                "arestdyfgh"
            ],
            "Line 2": [
                "sdgdsdsgds",
                "vjk"
            ],
            "Line 3": [
                "hgkguy",
                "ugiug"
            ],
            "Line 4": [
                "sdff",
                "fsadffffffffff"
            ],
            "Line 5": [
                "sfdaaaa"
            ]
        }


def test_ex2():
    assert check_validity(random_password()) == True


def test_ex3():
    my_deck = Deck()
    assert len(my_deck.get_cards()) == 40
    for card in my_deck:
        pass
    assert len(my_deck.get_cards()) == 0


def test_ex4():
    def sum1(x, y):
        return x + y

    assert my_reduce(sum1, [1, 2, 3, 4, 5], 10) == 25


def test_ex5():
    shapes = []
    results = []
    shapes.append(Circle(5))
    shapes.append(Circle(3))
    shapes.append(Square(3))
    shapes.append(Square(5))
    shapes.append(EquilateralTriangle(5))
    shapes.append(EquilateralTriangle(3))
    shapes.append(Rectangle(5, 3))
    shapes.append(Rectangle(2, 4))
    for shape in shapes:
        results.append((shape.calculate_area(), shape.calculate_perimeter()))
    assert results == [(78.53981633974483, 31.41592653589793),
                       (28.274333882308138, 18.84955592153876),
                       (9, 12),
                       (25, 20),
                       (27.95084971874737, 15),
                       (10.062305898749054, 9),
                       (15, 16),
                       (8, 12)]
