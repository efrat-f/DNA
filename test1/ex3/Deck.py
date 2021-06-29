from ex3.Card import Card


class Deck:
    def __init__(self):
        self.__cards = []
        for type1 in ["red", "blue", "green", "yellow"]:
            for i in range(1, 11):
                self.__cards.append(Card(type1, i))

    def shuffle(self):
        self.__cards.shuffle()

    def deal(self):
        return self.__cards.pop()

    def __iter__(self):
        self.__counter = 0
        self.__sum_card = len(self.__cards)
        return self

    def __next__(self):
        if self.__counter < self.__sum_card:
            card = self.deal()
            self.__counter += 1
            return card
        else:
            raise StopIteration

    def get_cards(self):
        return self.__cards
