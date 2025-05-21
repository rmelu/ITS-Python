import json
'''
PATH: str = "config.json"
mode: str = "r"


with open(PATH, mode=mode) as file:
    
    config: dict = json.load(file)
    print(config)

    #nome_applicazione: str = config["appName"]
    #print(nome_applicazione)'''


PATH: str = "config_1.json"
mode: str = "w"
config: dict = {}
with open(PATH, mode="r") as file:
    config = json.load(file)
'''
    config["server"]["host"] = "fecebook.com"
    config["server"]["port"] = 5000'''

with open(PATH, mode=mode) as file:

    config: dict = {"nome": "2048", "versione": "1.1.42", "05": "Android 16.1.0"}

    json.dump(config, file, indent=4)

    print(config)

    config["chiave_nuova"] = "valore_nuovo"