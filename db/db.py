class DB:
    def __init__(self):
        self.__ids = {}
        self.__names = {}

    def add_data(self, data):
        self.__ids[len(self.__ids)] = data
        self.__names[data.get_name()] = data

    def __len__(self):
        return len(self.__ids)

    def get_ids(self):
        return self.__ids

    def get_names(self):
        return self.__names

    def delete_obj(self, obj):
        del self.__ids[obj.get_id()]
        del self.__names[obj.get_name()]
