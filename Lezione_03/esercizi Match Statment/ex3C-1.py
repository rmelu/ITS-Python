voto_scolastico = int(input("Inserisci numero voto scolastico: "))
numero:list = ["10", "8 | 9", "7 | 6", "5 | 4", "3 | 1"]
match voto_scolastico:
        case 10:
            print("eccelente")
        case 8 | 9:
            print("Molto Buono")
        case 6 | 7:
            print("Sufficiente")
        case 4 | 5:
            print("Insufficiente")
        case 1 | 2 | 3:
            print("Gravemente insufficiente")
        case _:
            print("Voto non valido")


