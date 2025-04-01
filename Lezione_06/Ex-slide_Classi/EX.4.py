class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

food1 = Food("Pizza Margherita", 10.0, "Classic tomato and mozzarella pizza")
food2 = Food("Sushi Platter", 25.0, "Assorted fresh sushi and sashimi")
food3 = Food("Chocolate Cake", 8.0, "Rich choccolate cake with ganache")

class Menu:
    def __init__(self, foods=None):
        if foods is None:
            self.foods = []
        else:
            self.foods = foods

    def addFood(self, food):
        self.foods.append(food)

    def removeFood(self, food):
        if food in self.foods:
            self.foods.remove(food)

    def printPrices(self):
        for food in self.foods:
            print(f"{food.name}: ${food.price}")

    def getAveragePrice(self):
        if not self.foods:
            return 0   #restituisce 0 se non ci sono cibi nel menu
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)
    
menu = Menu([food1, food2])

menu.addFood(Food("Burger", 12.0, "Classic burger with fries"))
menu.addFood(Food("Salad", 9.0, "Fresh mixed greens with vinaigrette"))
print(menu.getAveragePrice())