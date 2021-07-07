import re


class dna_sequence:

    @staticmethod
    def __check_correct_nucleotide(sequence):
        for nucleotides in sequence:
            if nucleotides not in "TCGA":
                raise Exception("incorrect sequence")

    def __init__(self, sequence, number_id, name):
        self.__check_correct_nucleotide(sequence)
        self.__sequence = sequence
        self.__id = number_id
        self.__name = name
        print("create dna_sequence")

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, sequence):
        self.__check_correct_nucleotide(sequence)
        self.__sequence = sequence

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def insert(self, nucleotides, index):
        self.__check_correct_nucleotide(nucleotides)
        if index > len(self):
            raise Exception("incorrect index")
        self.__sequence = self.__sequence[:index] + nucleotides + self.__sequence[index:]

    def assignment(self, o: object):
        if type(o) == str:
            self.__sequence = o
        else:
            self.__sequence = o.get_sequence()

    def __str__(self) -> str:
        return "{" + f"sequence: {self.__sequence}" + "}"

    def __eq__(self, o: object) -> bool:
        return self.__sequence == o.get_sequence()

    def __ne__(self, o: object) -> bool:
        return self.__sequence != o.get_sequence()

    def __getitem__(self, item):
        return self.__sequence[item]

    def __setitem__(self, key, value):
        self.__check_correct_nucleotide(value)
        self.__sequence[key] = value

    def __len__(self):
        return len(self.__sequence)


# obj1 = dna_sequence("A")
# obj2 = dna_sequence("ATCGCCG")
# print(obj1 == obj2)
# print(obj1 != obj2)
# obj1.assignment(obj2)
# print(obj1 == obj2)
# print(obj1 != obj2)
# print(obj1.get_sequence())
# print(obj1.set_sequence("AGAATTCCC"))
# print(obj1.insert("A", 1))
# print(len(obj1))
# print(obj1.insert("C", 2))
# print(obj1)
