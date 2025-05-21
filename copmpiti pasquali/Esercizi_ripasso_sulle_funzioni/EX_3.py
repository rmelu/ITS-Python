from typing import List, Dict, Any

def rimuovi_elementi(lista: List[Any], da_rimuovere: Dict[Any, int]) -> List[Any]:
    """
    Elimina da una lista dati elementi specificati in un dizionario.

    Args:
        lista: La lista da cui rimuovere gli elementi.
        da_rimuovere: Un dizionario dove le chiavi sono gli elementi da rimuovere
                      e i valori sono il numero di volte che devono essere rimossi.

    Returns:
        Una nuova lista con gli elementi rimossi.
    """
    nuova_lista: List[Any] = list(lista) # Crea una copia per non modificare l'originale
    for elemento, count in da_rimuovere.items():
        try:
            for _ in range(count):
                nuova_lista.remove(elemento)
        except ValueError:
            # Se l'elemento non è più presente nella lista, ignora l'errore
            pass
    return nuova_lista

# Esempio di utilizzo (come nei tuoi test):
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1}))
print(rimuovi_elementi(['a', 'b', 'c', 'b'], {'b': 1}))
print(rimuovi_elementi([1, 2, 2, 3], {2: 3})) # Prova a rimuovere più volte di quanto presente'''

from typing import List, Dict

def rimuovi_elementi(lista: List[int], da_rimuovere: Dict[int, int]) -> List[int]:
    nuova_lista: List[int] = []
    conteggi = lista.copy() # Crea una copia per tenere traccia degli elementi presenti

    for elemento, quantita in da_rimuovere.items():
        count = conteggi.count(elemento)
        effettivamente_rimossi = min(quantita, count)
        for _ in range(effettivamente_rimossi):
            if elemento in conteggi:
                conteggi.remove(elemento)

    for elemento in lista:
        if elemento in conteggi:
            nuova_lista.append(elemento)

    return nuova_lista

# Esempio di utilizzo (come nei tuoi test):
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1}))






'''from typing import List, Dict

def rimuovi_elementi_alternativo(lista: List[int], da_rimuovere: Dict[int, int]) -> List[int]:
    nuova_lista: List[int] = []
    rimossi = {} 

    for elemento in lista:
        if elemento in da_rimuovere:
            rimossi_count = rimossi.get(elemento, 0)
            da_rimuovere_count = da_rimuovere[elemento]
            if rimossi_count < da_rimuovere_count:
                rimossi[elemento] = rimossi_count + 1
                continue 
        nuova_lista.append(elemento)

    return nuova_lista'''