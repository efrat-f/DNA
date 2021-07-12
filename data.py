class dna_data:
    def __init__(self):
        self.__dict_data = {}
        self.__num_data_obj = 0

    def insert_data(self, data):
        self.__dict_data[self.__num_data_obj] = data
        self.__num_data_obj += 1
