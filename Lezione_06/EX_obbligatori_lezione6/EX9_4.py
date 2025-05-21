class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"il ristorante {self.restaurant_name} serve cucina {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} è aperto! ")

    def set_number_served(self, number):
        self.set_number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

ristorante = Ristorante("La Taverna", "Italiana!")
print(f"\nClienti serviti inizialmente: {ristorante.number_served}")

ristorante.number_served = 15
print(f"\nClienti serviti dopo la modifica: {ristorante.number_served}!")

ristorante.set_number_served(50)
print(f"\nClienti serviti dopo set_number_served(): {ristorante.number_served} ")

ristorante.increment_number_served(15)
print(f"\nClienti serviti dopo increment_number_served(): {ristorante.number_served} <3 ")

