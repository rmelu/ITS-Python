#Dizionario originale (Ex 6-1 (esempio))
persona = {
    "first_name": "Pietro",
    "last_name": "Meloni",
    "age": 30,
    "city": "Sardegna"
} 
persona2 = {
    "first_name": "Mauro",
    "last_name": "Verdi",
    "age": 25,
    "city": "Milano"
} 
persona3= {
    "first_name": "Lidia",
    "last_name": "Polizzi",
    "age": 35,
    "city": "Calabria"
}

#Lista di persone (contenente tutti i dizionari)
persone = [persona, persona2, persona3]
for persona_singola in persone:   #persona_singola rappresentata un dizionario alla voltaint("informazioni su una persona:")
    print("informazioni su ogni persona:")

#   Stampa informazione di ogni persona 
    print(f"Nome: {persona_singola['first_name']}")
    print(f"Cognome: {persona_singola['last_name']}")
    print(f"Eta: {persona_singola['age']}")
    print(f"Città: {persona_singola['city']}\n")    # \n  per una riga vuota trale persone.