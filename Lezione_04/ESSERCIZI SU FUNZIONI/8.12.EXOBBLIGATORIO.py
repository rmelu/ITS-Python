#sandwich
'''def make_sandwich(*ingredienti):
    print("\nPreparo un panino con i seguenti ingredienti: ")
    for ingrediente in ingredienti:
        print(f"- {ingrediente}")  #serve per stampare ogni ingrediente su una nuova riga
        #print("- " + ", ".join(ingredienti))    #stampa tutti gli ingridienti

#chiamo la funzione con diversi numeri di argometri 
make_sandwich('tacchino', 'spinaci', 'mozzarella')
make_sandwich('pollo', 'insalata', 'pomodoro', 'chedar', 'salsa a piacere')   
make_sandwich('tonno', 'pomodoro', 'insalate', 'cetriolo', 'maionese')
make_sandwich('prosciutto crudo', 'formaggio')
print("\nIl tuo panino è pronto! Buon appetito. ")
print()'''

#altrimenti possiamo scrivere cosi
def make_sandwich(ingredienti):
    lista_ingredineti = []
    for ingrediente in ingredienti:
        lista_ingredineti.append(ingrediente)          #aggiungo l'ingrediente alla lista
    return lista_ingredineti    #restituisco la lista completa
print("\nPreparo un panino con i seguenti ingredienti: ")
ingredienti = [
    "1° PANINO:", 
    "tacchino",
    "avocado",
    "pomodoro",
    "maionese",
    "2° PANINO:"
    "pollo",
    "pomodoro",
    "insalata",
    "maionese", 
    "3° PANINO:",
    "prosciutto cotto",
    "formaggio",
    "rucola",
]
lista_panino = make_sandwich(ingredienti)
print(lista_panino)   #stampa lista panino
print("\nIl tuo panino è pronto! Buon appetito. ")
print()
