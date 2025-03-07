numero_neonati = int(input("inserisci il numero di neonati: "))
match numero_neonati:
    case 1:
        print("Congratulazione! :-) ")
    case 2:
        print("Wow Gemelli! :) ")
    case 3:
        print("Wow tre! :o ") 
    case 4:
        print("Mamma mia quattro! WOW ;-* ")
    case 5: 
        print("Incredibile! Cinque!! Complimenti ;))")
    case _:
        print(f"Non ci credo! {numero_neonati} bambini! ")