class dna_sequence:
    def __init__(self, sequence):
        self.__sequence = sequence

    def get_sequence(self):
        return self.__sequence

    def set_sequence(self, sequence):
        self.__sequence = sequence

    def insert(self, nucleotides, index):
        if index > len(self)-1:
            print("incorrect index")
            return
        try:
            self.__sequence = self.__sequence[:index] + nucleotides + self.__sequence[index+1:]
        except TypeError as e:
            print("ERROR: given params not correct")

    def assignment(self, o: object):
        if type(o) == str:
            self.__sequence = o
        elif type(o) == dna_sequence:
            self.__sequence = o.get_sequence()
        else:
            print("object to assign not fit correct")

    def __str__(self) -> str:
        return "{" + f"sequence: {self.__sequence}" + "}"

    def __eq__(self, o: object) -> bool:
        if type(o) == dna_sequence:
            return self.__sequence == o.get_sequence()
        else:
            print("object to assign not fit correct")

    def __ne__(self, o: object) -> bool:
        if type(o) == dna_sequence:
            return self.__sequence != o.get_sequence()

        else:
            print("object to assign not fit correct")

    def __getitem__(self, item):
        return self.__sequence[item]

    def __setitem__(self, key, value):
        self.__sequence[key] = value

    def __len__(self):
        return len(self.__sequence)


# obj1 = dna_sequence("dff")
# obj2 = dna_sequence("rerr")
# print(obj1 == obj2)
# print(obj1 != obj2)
# obj1.assignment(obj2)
# print(obj1 == obj2)
# print(obj1 != obj2)
# print(obj1.get_sequence())
# print(obj1.set_sequence("sdd"))
# print(obj1.insert("7", 5))
# print(obj1.insert(5, 2))
# print(len(obj1))
# print(obj1.insert("q", 2))
# print(obj1)
