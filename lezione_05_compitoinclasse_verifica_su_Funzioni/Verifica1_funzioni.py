def somma_elementi(lista1, lista2):
    if len(lista1) != len(lista2):
        return None
    risultato = []
    for i in range(len(lista1)):
        risultato.append(lista1[i] + lista2[i])
    return risultato
    
print(somma_elementi([1, 1, 1], [1, 1, 1]))