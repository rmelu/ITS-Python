class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"il ristorante {self.restaurant_name} serve cucina {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"il ristorante {self.restaurant_name} è aperto! ")

ristorante = Ristorante("La Taverna", "italiana")
print(f"Nome del ristorante: {ristorante.restaurant_name}")
print(f"Tipo di cucina: {ristorante.cuisine_type}")

ristorante.describe_restaurant()
ristorante.open_restaurant()



