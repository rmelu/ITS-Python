def even_odd_pattern(lista):
    pari = []
    dispari = []
    for numero in lista:
        if numero %2 == 0:
            pari.append(numero)
        else:
             dispari.append(numero)
    return pari + dispari