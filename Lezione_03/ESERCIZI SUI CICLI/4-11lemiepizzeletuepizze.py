mie_pizze = ['Peperoni', 'Margherita', 'Vegetariana']
friend_pizzas = mie_pizze[:]    #[:] crea una nuova lista, non un riferimento alla stessa

mie_pizze.append("Capricciosa")
friend_pizzas.append("Funghi e salsiccia")

print("Le mie pizze preferite sono")
for pizza in friend_pizzas:
    print(pizza)