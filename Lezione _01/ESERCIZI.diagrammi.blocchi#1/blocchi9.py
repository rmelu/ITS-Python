#classifica delle vendite
nome = input("Inserisci il nome: ")
vendite = float(input("Inserisce le vendite: "))
max__nome = nome
max_vendite = vendite
min_nome = nome
min_vendite = vendite
cont = 0
#ciclo principale
while cont < 5:
    nuovo_nome = input("Inserisci il nome: ")
    nuovo_vendite = float(input("Inserisci le nuove vendite: "))

    if nuovo_vendite > max_vendite:
        max_nome = nuovo_nome
        max_vendite = nuovo_vendite

    if nuovo_vendite < min_vendite:
        min_nome = nuovo_nome
        min_vendite = nuovo_vendite
        cont += 1
  #stampa i risultati      
print("Nome con vendite massime:", max_nome)
print("Vendite massime:", max_vendite)
print("Nome con vendite minime:", min_nome)
print("Vendite minime:", min_vendite)