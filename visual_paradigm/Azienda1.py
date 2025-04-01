#PRIMO TENTATIVO 
class Impiegato:
    def __init__(self, nome, cognome, data_nascita,stipendio, altro=None):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.stipendio = stipendio
        self.altro = altro

class Dipartimento:
    def __init__(self, nome, num_telefono):
        self.nome = nome
        self.num_telefono = num_telefono
class Progetto:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget

impiegati = [
    Impiegato("Pascal", "Sovage:", "10/08/1998", 2300),
    Impiegato("Aiscia", "Jasmin:", "15/09/1970", 1100)
]
dipartimenti = [
    Dipartimento("Azienda.Spa1:", "06 678990,  345 675 9830")
]

progetti = [
    Progetto("Inovazione:", 30000000)
]

for impiegato in impiegati:
    print(impiegato.nome, impiegato.cognome, impiegato.data_nascita, impiegato.stipendio)
for dipartimento in dipartimenti:
    print(dipartimento.nome, dipartimento.num_telefono)
for progetto in progetti:
    print(progetto.nome, progetto.budget)




