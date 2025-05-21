
#dal fail persona.py importa la classe Persona
from persona import Persona
#creare un oggetto di tipo persona
rm:Persona = Persona("rahel", "melu", 34)    #è la chiamata costrutore cioè il nome cognome ed età
print(rm)

print(rm.name, rm.lastname, rm.age)

#dal fail persona2.py importa la classe persona
from persona2 import Persona

rm:Persona = Persona("rahel", "melu", 34)

#voglio richiamare la funzione displayData della cklasse persona per stampare in output le informazioni relative alla persona rm
print("---------")
rm.displayData()

#impostare il nome della persona rm
rm.setName("rahel")
print("-----------")
rm.displayData()

#importare il cognome della persona rm
rm.setlastname("melu")

#importa l'eta della persona rm
rm.setage(34)

print("--------")
rm.displayData()

print("--------")

print(rm.getName(), rm.getlastname(), rm.getage())    #get ~~~~~ritorna
                                                    #self ~~~~~~imposta