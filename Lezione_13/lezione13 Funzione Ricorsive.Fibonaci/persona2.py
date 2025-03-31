class Persona: 
    def __init__(self, name, lastname, age):
        self.name = ""
        self.lastname = ""
        self.age = 34

    #funzione che mostri in output i dati relativi ad una persona:
    def displayData(self):
        print(f"Name: {self.name}\nCognome: {self.lastname}\nage: {self.age}")

    #una funzione che ci consenta impostare il valore de self.name

    def setName(self, name:str) -> None:
        self.name = name


    def setlastname(self, lastname:str) -> None:
        self.lastname = lastname


    def setage(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age =age

    #funzione che mi permette di ritornare il valore di sel.name
    def getName(self) -> str:
        return self.name

    #funzione che mi permette di ritornarte il valore self.lastname
    def getlastname(self) -> str:
        return self.lastname

    #funzione che mi consente di ritrovare il valore di self.age
    def getage(self) -> int:
        return self.age
        