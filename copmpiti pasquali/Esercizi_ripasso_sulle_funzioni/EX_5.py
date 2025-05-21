from typing import Dict

def filtra_e_mappa(prodotti: Dict[str, float]) -> Dict[str, float]:
    risultato: Dict[str, float] = {}
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            prezzo_scontato = prezzo * 0.9
            risultato[prodotto] = prezzo_scontato
    return risultato

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
