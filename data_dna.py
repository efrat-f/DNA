class Data_dna():
    def __init__(self):
        self.__ids = {}
        self.__names = {}

    def add_dna_sequence(self, dna_sequence):
        self.__ids[dna_sequence.get_id()] = dna_sequence
        self.__names[dna_sequence.get_name()] = dna_sequence

    def __len__(self):
        return len(self.__ids)

    def get_ids(self):
        return self.__ids

    def get_names(self):
        return self.__names

    def delete_obj(self, obj):
        del self.__ids[obj.get_id()]
        del self.__names[obj.get_name()]

