class Ristorante:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"il ristorante {self.restaurant_name} serve cucina {self.cuisine_type}.")

Ristorante1 = Ristorante("La Taverna", "Italiana")
Ristorante2 = Ristorante("Tacos Piccanti", "Mexicana")
Ristorante3 = Ristorante("Sushi Zen", "Giappone")

Ristorante1.describe_restaurant()
Ristorante2.describe_restaurant()
Ristorante3.describe_restaurant()