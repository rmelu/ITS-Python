def clasifica_numeri(lista_numeri):
    dizionario_classificato = {
        "positivi": [],
        "negativi": []
    }
    for numero in lista_numeri:
        if numero >= 0:
            dizionario_classificato["positivi"].append(numero)
        else:
            dizionario_classificato["negativi"].append(numero)
    return dizionario_classificato

numeri_di_esempio = [1, -2, 3, 0, -5, 5, -10.5, 7.2]
risultato = clasifica_numeri(numeri_di_esempio)
print(risultato)
