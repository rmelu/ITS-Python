mammiferi = ['cane', 'gatto', 'cavallo', 'elefante', 'leone', 'balena', 'delfino']
rettili = ['serpente', 'lucertola', 'tartaruga', 'coccodrillo']
uccelli = ['aquila', 'pappagallo', 'gufo', 'falco', 'cigno', 'anatra', 'gallina', 'tacchino']
pesci = ['squalo', 'trota', 'salmone', 'capra']

animali = { #Definizione per memorizzare le info
    "nome": "",
    "tipo": "",
    "habitat": ""
}

animali["nome"] = input("Digita il nome di un animale:  ")
animali["habitat"] = input(f"Digita l'habitat in cui vive l'animale {animali['nome']}:  ") 

match animali["nome"]:
    case animale if animale in mammiferi:
        animali["tipo"] = "Mammifero"
        print(f"{animali['nome']} appartiene alla categoria dei Mammiferi!")
    case animale if animale in rettili:
        animali["tipo"] = "Rettili"
        print(f"{animali['nome']} appartiene alla categoria dei Rettili!")
    case animale if animale in uccelli:
        animali["tipo"] = "Uccelli"
        print(f"{animali['nome']} appartiene alla categoria dei Uccelli!")
    case animale if animale in pesci:
        animali["tipo"] = "Pesce"
        print(f"{animali['nome']} appartiene alla categoria dei Pesci!")
    case _:
        print(f"Non so dire in quale categoria classsificare l'animale {animali['nome']}! ")

match animali["tipo"]:
    case "Mammifero":
        match animali["nome"]:
            case "balena" | "delfino":
                match animali['habitat']:
                    case "acqua":
                        print(f"L'animale {animali['nome']} è uno dei mammiferi che può vivere in acqua!")
                    case _:
                        print(f"Non ho mai visto l'animale {animale['noome']} vivere nell'habitat {animale['habitat']}. ")
            case "cane" | "gatto" | "cavallo" | "elefante" | "leone":
                match animali["habitat"]:
                    case "terra":
                         print(f"L'animale {animali['nome']} è uno dei mammiferi che può vivere sulla terra! ")
                    case _:
                         print(f"Non ho mai visto l'animale {animale['nome']} vivere nell'habitat {animale['habitat']}")
    case "Rettile":
        match animali["habitat"]:
            case "terra" | "acqua":
                print(f"L'animale {animale['nome']} è uno dei rettili che può vivere sia sulla terra che in acqua!")
            case _:
                print(f"Non ho mai visto l'animale {animale['nome']} vivere nell'habitat {animale['habitat']}. ")
    case "Uccelli":
        match animali["habitat"]:
            case "terra" | "aria":
                print(f"L'animale {animale['nome']} è uno dei uccelli che può vivere sia in aria che sulla terra!")
            case _:
                print(f"Non ho mai visto l'animale {animale['nome']} vivere nell'habitat {animale['habitat']}.")
    case "Pesce":
        match animali["habitat"]:
            case "acqua":
                print(f"L'animale {animali['nome']} è uno dei pesci che può vivere in acqua!")
            case _:
                print(f"Non ho mai visto l'animale {animale['nome']} vivere nell'habitat {animale['habitat']}.")
    case "Sconoscito":
        print(f"Non sono in grado di fornire sull'habitat {animale['habitat']}.")
print('Fine del programma, torna a trovarci <3')  #Stampa il dizionario alla fine (opzionale)

