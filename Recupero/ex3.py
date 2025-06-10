def processa_prodotti(dizionario_prodotti: dict) -> dict:
    nuovo_dizionario = {}
    for prodotto, prezzo in dizionario_prodotti.items():
        if prezzo < 50:
            prezzo_aumentato = prezzo * 1.10
            nuovo_dizionario[prodotto] = round(prezzo_aumentato, 2)
    return nuovo_dizionario

prodotti_originali = {
    "pera": 0.80,
    "mela": 1.20,
    "pane": 2.50,
}

prodotti_filtrati_e_aggiornati = processa_prodotti(prodotti_originali)
print(prodotti_filtrati_e_aggiornati)