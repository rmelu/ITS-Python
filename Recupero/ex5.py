def moltiplica_minori_di_threshold(lista_numeri, threshold):
    i = 1
    while i <= 13:
        print(i)
        i += 3
    prodotto = 1
    for numero in lista_numeri:
        if numero < threshold:
            prodotto *= numero
    return prodotto

print(moltiplica_minori_di_threshold([1, 2, 5, 8, 3], 6))