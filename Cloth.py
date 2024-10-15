from abc import ABC


class Cloth(ABC):
    __name: str

    def __init__(self, name: str):
        self.__name = name

    @property
    def Name(self) -> str:
        return self.__name

    def __repr__(self):
        return self.__name
