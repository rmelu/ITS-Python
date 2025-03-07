#Creo i dizionari per ohni animale domestico
animale1 = {
    "tipo": "cane",
    "proprietario": "Lola",
}
animale2 = {
    "tipo": "gatto",
    "proprietario": "Chiara",
}
animale3 = {
    "tipo": "pesce rosso",
    "proprietario": "Rachele"
}
#Crea una lista contenente i dizionari
animali_domestici = [animale1, animale2, animale3]

#Ciclo attraverso la lista e stampo le informazioni
for animale in animali_domestici:
    print("informazioni sull'animali:")
    print("Tipo:", animale["tipo"])
    print("proprietario:", animale["proprietario"])
    print() #stampa una riga vuota per sapere gli animali 