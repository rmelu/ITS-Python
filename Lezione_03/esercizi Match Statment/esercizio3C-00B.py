nome = input("Inserisce nome: ")
genere = input("Inserire gender. Digitare m per maschio e f per femmina: ")

match genere:
    case "m":
        print(f"Nome: {nome}")
        print("Gender : Maschio")
    case "f":
        print(f"Nome: {nome} ")
        print("Gender : Femmina")
    case _:
        print("Errore: Imposibile generare un documento di identità con questo genere.")
