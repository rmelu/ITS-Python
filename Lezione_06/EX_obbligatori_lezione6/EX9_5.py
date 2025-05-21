class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nInfomation Utente: ")
        print(f" Name: {self.first_name} {self.last_name}")
        print(f" Age: {self.age}")
        print(f" City: {self.city}")
        print(f" Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Ciao {self.first_name} {self.last_name}! ")
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User ("Mario", "Rossi", 30, "Roma")
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)