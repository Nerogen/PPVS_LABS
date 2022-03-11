import pickle
from Lab1.interfaces.write import Writer
from Lab1.interfaces.read import Reader


class Serialization(Writer, Reader):

    @staticmethod
    def write(some_objects, file_name: str):
        with open(file_name, 'wb') as file:
            pickle.dump(some_objects, file)

    @staticmethod
    def read(file_name: str):
        with open(file_name, 'rb') as file:
            some_object = pickle.load(file)
        return some_object
