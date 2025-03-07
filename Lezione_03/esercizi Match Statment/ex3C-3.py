oggetti = []
#riempimento della lista con tre oggetti.
for i in range(3):
    oggetto = input(f"inserisci l'oggeto {i+1}:")
    oggetti.append(oggetto)

print(oggetti)

#Classifica degli oggetti con match
match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Prodotti allimentari")
    case ["sedia","tavolo", "armadio"]:
       print("Mobili")
    case ["telefono","computer","tablet"]:
        print("Dispositivi eletronici") 
    case _:
        print("Categoria sconosciuta")