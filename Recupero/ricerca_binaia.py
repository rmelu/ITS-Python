from typing import List
def ricerca_binaria(lista: List[int], numero: int) -> bool:
    """
    Effetua la ricerca binaria in una list di numeri interi ordinati.
    Ritorna True se il numero è presente nella lista, altrimenti False.
    
    :parametri lista: Lista[int] - Lista di numeri interi ordinati
    :parametri numero: int - Numero da cercare nella lista
    :return:bool -True se il numero è presente, False altrimenti."""

    sinistra, destra = 0, len(lista) - 1    #immagina da 0 a 100 ma in questo caso sarrebbe da 0 a 99 (//: divisione intera) (/ : floot ovvero divisione normale con virgola) (%: modulo, ovvero  restituisce il resto di una divisione))
    
    while sinistra <= destra:
        centro = (sinistra + destra) // 2
        if lista[centro] == numero:
            return True
        elif lista[centro] < numero:
            sinistra = centro + 1
        else:
            destra = centro - 1
            
    return False
print(ricerca_binaria([1, 2, 3, 4, 5], 3))  # True 
print(ricerca_binaria([1, 2, 3, 4, 5], 6))  # False
print(ricerca_binaria([10, 20, 30, 40, 50], 25))  # False
print(ricerca_binaria([10, 20, 30, 40, 50], 30))  # True
print(ricerca_binaria([], 1))  # False
print(ricerca_binaria([5], 5))  # True
print(ricerca_binaria([5], 10))  # False
print(ricerca_binaria([1, 3, 5, 7, 9], 1))  # True
print(ricerca_binaria([1, 3, 5, 7, 9], 2))  # False