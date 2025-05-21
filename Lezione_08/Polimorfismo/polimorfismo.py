from persona import Persona
from alieno import Alieno

#creare l'oggetto p della classe persona
p: Persona = Persona("rahel", "melu", 34)

#visualizzare le informazione relative alla persona p
print(p)

#creare un oggetto della classe Alieno
et:Alieno = Alieno("Andromeda")

#visualizzare le informazioni relative all'Alieno et
print(et)

#l'oggetto p invoca il metodo speak()
p.speak()

#loggetto et invoca il metodo speak()
et.speak()