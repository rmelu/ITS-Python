from typing import List, Dict

def classifica_numeri(lista: List[int]) -> Dict[str, List[int]]:
    pari: List[int] = []
    dispari: List[int] = []
    for numero in lista:
        if numero % 2 == 0:
            pari.append(numero)
        else:
            dispari.append(numero)
    return {'pari': pari, 'dispari': dispari}

# Esempio di utilizzo (come nel tuo test):
print(classifica_numeri([1, 2, 3, 4, 5, 6]))
print(classifica_numeri([]))