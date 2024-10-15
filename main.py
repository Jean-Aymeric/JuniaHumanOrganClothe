from Boxer import Boxer
from Human import Human
from Shirt import Shirt

toto = Human("Ashkelad")
print(toto.Name)
print(toto)
toto.addCloth(Shirt())
toto.addCloth(Shirt())
toto.addCloth(Boxer())
print(toto.Clothes)
print(toto)
