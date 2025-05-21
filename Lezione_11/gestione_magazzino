class Prodotto:
    """
    Rappresenta un prodotto con nome e quantità.
    """
    def __init__(self, nome: str, quantità: int):
        # Validiamo l'input per assicurarci che nome non sia vuoto e quantità non sia negativa.
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Il nome del prodotto non può essere vuoto.")
        if not isinstance(quantità, int) or quantità < 0:
            raise ValueError("La quantità del prodotto deve essere un intero non negativo.")

        self.nome = nome.strip()
        self.quantità = quantità

    def __str__(self):
        """Restituisce una rappresentazione del prodotto facile da leggere."""
        return f"Prodotto: {self.nome}, Quantità: {self.quantità}"

    def __eq__(self, other):
        """
        Definisce come due oggetti Prodotto vengono confrontati per l'uguaglianza.
        Sono uguali se i loro nomi sono gli stessi (ignorando maiuscole/minuscole).
        """
        if not isinstance(other, Prodotto):
            return NotImplemented
        return self.nome.lower() == other.nome.lower()

    def __hash__(self):
        """
        Rende gli oggetti Prodotto 'hashable', permettendone l'uso come chiavi nei dizionari
        o l'archiviazione nei set. L'hashing si basa sul nome del prodotto (ignorando maiuscole/minuscole).
        """
        return hash(self.nome.lower())


class Magazzino:
    """
    Gestisce l'inventario dei prodotti nel magazzino.
    """
    def __init__(self):
        # Useremo un dizionario per memorizzare i prodotti, con il nome normalizzato
        # del prodotto come chiave. Questo rende la ricerca molto veloce.
        self.prodotti = {} # Formato: {nome_prodotto_normalizzato: oggetto_prodotto}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        """
        Aggiunge un prodotto al magazzino. Se il prodotto esiste già,
        la sua quantità viene aggiornata aggiungendo la nuova quantità.
        """
        if not isinstance(prodotto, Prodotto):
            print("Errore: L'oggetto deve essere un'istanza della classe Prodotto.")
            return

        nome_normalizzato = prodotto.nome.lower()
        if nome_normalizzato in self.prodotti:
            self.prodotti[nome_normalizzato].quantità += prodotto.quantità
            print(f"Quantità aggiornata per '{prodotto.nome}'. Nuova quantità: {self.prodotti[nome_normalizzato].quantità}")
        else:
            self.prodotti[nome_normalizzato] = prodotto
            print(f"Prodotto '{prodotto.nome}' aggiunto con quantità {prodotto.quantità}.")

    def cerca_prodotto(self, nome: str) -> Prodotto | None:
        """
        Cerca un prodotto per nome e lo ritorna se esiste, altrimenti None.
        """
        if not isinstance(nome, str) or not nome.strip():
            print("Errore: Il nome del prodotto da cercare non può essere vuoto.")
            return None

        nome_normalizzato = nome.strip().lower()
        if nome_normalizzato in self.prodotti:
            print(f"Prodotto '{nome}' trovato.")
            return self.prodotti[nome_normalizzato]
        else:
            print(f"Prodotto '{nome}' non trovato in magazzino.")
            return None

    def verifica_disponibilità(self, nome: str) -> str:
        """
        Verifica la disponibilità di un prodotto in magazzino e ne restituisce lo stato della quantità.
        """
        if not isinstance(nome, str) or not nome.strip():
            return "Errore: Il nome del prodotto da verificare non può essere vuoto."

        nome_normalizzato = nome.strip().lower()
        if nome_normalizzato in self.prodotti:
            quantità = self.prodotti[nome_normalizzato].quantità
            if quantità > 0:
                return f"Il prodotto '{nome}' è DISPONIBILE. Quantità: {quantità}."
            else:
                return f"Il prodotto '{nome}' è ESAURITO."
        else:
            return f"Il prodotto '{nome}' non è presente in magazzino."

    def mostra_inventario(self):
        """Mostra tutti i prodotti attualmente in magazzino."""
        print("\n--- Inventario Magazzino ---")
        if not self.prodotti:
            print("Il magazzino è vuoto.")
            return
        for prodotto in self.prodotti.values():
            print(prodotto)
        print("----------------------------")

# Il gestore del magazzino crea un nuovo magazzino
mio_magazzino = Magazzino()

# Creazione di vari prodotti con diverse quantità
print("--- Aggiunta Prodotti ---")
prodotto1 = Prodotto("Laptop", 10)
prodotto2 = Prodotto("Mouse Wireless", 50)
prodotto3 = Prodotto("Tastiera Meccanica", 25)
prodotto4 = Prodotto("Monitor 27 pollici", 15)
prodotto5 = Prodotto("laptop", 5) # Un prodotto con lo stesso nome ma diversa capitalizzazione

# Aggiunge i prodotti al magazzino
mio_magazzino.aggiungi_prodotto(prodotto1)
mio_magazzino.aggiungi_prodotto(prodotto2)
mio_magazzino.aggiungi_prodotto(prodotto3)
mio_magazzino.aggiungi_prodotto(prodotto4)
mio_magazzino.aggiungi_prodotto(prodotto5) # Questo dovrebbe aggiornare la quantità di "Laptop"
print("\n" + "="*30 + "\n")

# Mostra l'inventario attuale
mio_magazzino.mostra_inventario()
print("\n" + "="*30 + "\n")

# Il sistema cerca un prodotto per verificare se esiste nell'inventario
print("--- Ricerca Prodotti ---")
cerca_laptop = mio_magazzino.cerca_prodotto("Laptop")
if cerca_laptop:
    print(f"Dettagli trovato: {cerca_laptop}")

cerca_cuffie = mio_magazzino.cerca_prodotto("Cuffie Gaming") # Un prodotto non esistente
print("\n" + "="*30 + "\n")

# Il sistema verifica la disponibilità dei prodotti in inventario
print("--- Verifica Disponibilità ---")
print(mio_magazzino.verifica_disponibilità("Mouse Wireless"))
print(mio_magazzino.verifica_disponibilità("Tastiera Meccanica"))
print(mio_magazzino.verifica_disponibilità("Monitor 27 pollici"))

# Mettiamo un prodotto a zero per testare lo stato "esaurito"
prodotto_esaurito = Prodotto("Webcam HD", 0)
mio_magazzino.aggiungi_prodotto(prodotto_esaurito)
print(mio_magazzino.verifica_disponibilità("Webcam HD"))
print(mio_magazzino.verifica_disponibilità("Cavo HDMI")) # Un prodotto non presente nel magazzino
print("\n" + "="*30 + "\n")

# Esempio di gestione degli input non validi
print("--- Test Input Non Validi ---")
mio_magazzino.aggiungi_prodotto("non è un oggetto prodotto") # Tentativo di aggiungere un oggetto non-Prodotto
mio_magazzino.cerca_prodotto("") # Ricerca con un nome vuoto
print(mio_magazzino.verifica_disponibilità("")) # Verifica disponibilità con un nome vuoto

