#Definizione degli animali con una carrateristica  comune
animali = ["Cane", "Gatto", "Cavallo"]

#Stampare dei nomi degli animali
print("Animali con una carrateristica comune:")
for animale in  animali:
    print(animale)
# Stampa di una dichiarazione su ogi animale
print("\n Dichiarazione sugli animali:")
for animale in animali:
    if animale == "Cane":
        print(f"Un {animale} sarebbe un ottimo compagno per la vita <3.")
    elif animale == "Gatto":
        print(f"Un {animale} sarebbe un ottimo compagno per chi ama la tranquillita ;-).")
    elif animale == "Cavallo":
        print(f"Un {animale} sarebbe un ottimo compagno per chi ama l'equitazione. :>")

#Stampare delle carrateristiche in comune 
print("\n Questi animali hanno in comune il fatto di essere spesso considerati animali domestici o da compagnia.") 
