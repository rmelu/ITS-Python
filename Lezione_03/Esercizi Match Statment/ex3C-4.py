mammiferi = ['cane', 'gatto', 'cavallo', 'ellefante', 'leone']
rettili = ['serpente', 'lucertona', 'tartaruga', 'coccodrillo']
uccelli = ['aquila', 'pappagallo', 'gufo', 'falco']
pesci = ['squalo', 'trota', 'salmone', 'capra']

animale = input("Digita il nome di un animale: ")

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartenente alla categoria dei Mammifer!")
    case animale if animale in rettili:
        print(f"{animale} appartenente alla categoria di Rettili!")
    case animale if animale in uccelli:
        print(f"{animale} appartenente alla categoria uccelli!")
    case animale if animale in pesci:
        print(f"{animale} appartenente alla categoroia di pesci!")
    case _: 
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")
        