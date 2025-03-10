#classifica delle vendite
nome = input("Inserisci il nome: ")
vendite = float(input("Inserisce le vendite: "))
max__nome = nome
max_vendite = vendite
min_nome = nome
min_vendite = vendite
#ciclo forper elaborazione 20 coppie nome-vendite
for i in range(19):
    nuovo_nome = input("Inserisci il nome: ")
    nuovo_vendite = float(input("Inserisci le nuove vendite: "))

    if nuovo_vendite > max_vendite:
        max_nome = nuovo_nome
        max_vendite = nuovo_vendite

    if nuovo_vendite < min_vendite:
        min_nome = nuovo_nome
        min_vendite = nuovo_vendite

  #stampa i risultati      
print("Venditore con vendite massime:", max__nome, "Vendite:", max_vendite)
print("Venditore con vendite minime:", min_nome, "Vendite:", min_vendite)
