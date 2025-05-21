class User:
    def __init__(self, first_name, last_name, age, city, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.occupation = occupation

    def describe_user(self):
        print(f"\nInfomation Utente: ")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" City: {self.city}")
        print(f" Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Ciao {self.first_name} {self.last_name}! ")
        print()

User1 = User ("Mario", "Rossi", 30, "Roma", "Ingegnere")
User2 = User ("Lia", "Belli", 16, "Firenze", "Studentessa")
User3 = User ("Tomas", "Bianch", 25, "Venezia", "Pilota")
User4 = User ("Federico", "Verdi", 29, "New York", "Insegnante")

User1.describe_user()
User1.greet_user()

User2.describe_user()
User2.greet_user()

User3.describe_user()
User3.greet_user()

User4.describe_user()
User4.greet_user()
                                 