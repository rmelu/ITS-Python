class Persona:
    '''di una persona dobbiamo sapere delle informazioni.
    queste informazioni vengono chiamate attributi (della classe persona)
    le informazinoni saranno:
    '-nome'
    '-cognome'
    '-età''
    
     come li rappresento in python?'
    
    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)'''
#contributo'
def __init__(self,name:str, lastname:str, age:int):                           #init significa inizializzazione,~~~~~#self in inglese significa me stesso
    self.setName(name)
    self.setLastname(lastname)
    self.setAge(age)


    #il metodo speak() per la classe Persona che consente di simulare un saluto
def speak(self) -> None:
    print(f"\nHello my name is {self.getName()}!\n")                                                     