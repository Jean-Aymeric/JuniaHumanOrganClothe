from Cloth import Cloth
from Heart import Heart
from Organ import Organ


class Human:
    __name: str
    __clothes: [Cloth]
    __organs: [Organ]

    def __init__(self, name: str):
        self.__organs = []
        self.__organs.append(Heart())
        self.__name = name
        self.__clothes = []

    @property
    def Name(self) -> str:
        return self.__name

    def addCloth(self, cloth: Cloth):
        self.__clothes.append(cloth)

    @property
    def Clothes(self) -> [Cloth]:
        return self.__clothes

    def __repr__(self):
        return "je m'appelle " + self.__name + " et je porte " + str(self.Clothes)
