import saluto
saluto.greet("rahel")



import saluto as s          #as serve per rinominare
s.greet("rahel.ricordati che un secondo tentativo")



#se vuoi importare solo la funzione greet dal saluto ed ignorare il resto del modulo saluto farò:
from saluto import greet
greet("rahel")


from saluto import greet as g
g("Alice")