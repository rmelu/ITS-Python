class persona:
    def __init__ (self,name:str, lastname:str, age:int):
        self.setName(name)
        self.setlastname(lastname)                                                          #get ritorna
        self.setAge(age)                                                                    #set restituisce

# metodo spieciale che ritorna una stringa e che viene chiamata automaticamente quando si usa l'istruzione print(obj),
# dove obj è oggetto della classe persona 
# funzione che mi mostri in output i dati relativi ad una persona
    def __str__(self) -> str:
        return (f"Nome: {self.name} \nCognome: {self.lastname}\nEtà: {self.age}")
    
# il metodo __call__ mi consente di usare l'oggetto della classe Persona istanziato come una funzione
# QUindi, un oggetto mi mostri in output i dati relativi ad una persona.
    
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} è minorenne! ") 
        elif 18 <= self.age < 30:
            print(f" {self.name} {self.lastname} è maggiorenne ovvero abbastanza adulto di fare ciò che vuole! ")
        else:
            print(f"{self.name} {self.lastname}")