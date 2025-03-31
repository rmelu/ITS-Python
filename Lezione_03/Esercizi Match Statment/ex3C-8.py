frase = input("Bellissima: ")
match frase:
    case frase if frase.endswith("?") and len(frase) % 2 == 0:
        print("si")
    case frase if frase.endswith("?") and len(frase) % 2 != 0:
        print("no")
    case frase if frase.endswith("!"):
        print("oh!")
    case _:
        print(f"Tu dici {frase}.")
