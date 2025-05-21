import json
# Definire dizionare in python 
mio_dizionario = {
    "nome": "Lilly",
    "cognome": "Bianchi",
    "Eta": 25,
    "Città": "Roma",
    "Interessi": ["Calcio", "Cinema", "Nuoto", "Cucina"],
    "Professione": "Studente",
    "altre_info": "None"
}


PATH: str = "config.json"
mode: str = "r"

with open(PATH, mode=mode) as file:
    config = json.load(file)
    print(mio_dizionario)

config["nome"] = "Flavio"

with open(PATH, mode="w") as file:

    json.dump(config, file, indent=4)