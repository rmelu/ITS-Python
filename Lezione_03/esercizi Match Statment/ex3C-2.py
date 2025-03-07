voto_laurea = int(input("Inserisci il voto: "))

match voto_laurea:
        case voto_laurea if 106 <= voto_laurea and voto_laurea <= 110:    # 106 <= voto_laurea <= 110 -> voto_laurea è compreso tra 106 e 110
            print("GPA 4.0")
        case voto_laurea if 101 <= voto_laurea and voto_laurea <= 105:                        
            print("GPA 3.7")
        case voto_laurea if 96 <= voto_laurea and voto_laurea <= 100:
            print("GPA 3.3")
        case voto_laurea if 91 <= voto_laurea and voto_laurea <= 95:                                           
            print("GPA 3.0")
        case voto_laurea if 86 <= voto_laurea and voto_laurea <= 90:
            print("GPA 2.7")
        case voto_laurea if 81 <= voto_laurea and voto_laurea <= 85:
            print("GPA 2.3")
        case voto_laurea if 76 <= voto_laurea and voto_laurea <= 80:
            print("GPA 2.0")
        case voto_laurea if 70 <= voto_laurea and voto_laurea <= 75:
            print("GPA 1.7")
        case voto_laurea if 66 <= voto_laurea and voto_laurea <= 69:
            print("GPA 1.0")
        case _:
            print(" Voto non valido ")
            print("Tenta la prossima volta mi dispiace")
            print()