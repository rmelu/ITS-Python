class Film:
    """
    Rappresenta un film con titolo e durata.
    """
    def __init__(self, titolo: str, durata: str):
        if not isinstance(titolo, str) or not titolo.strip():  #strip toglie tutti gli spazzi ho cose superflui lasciando solo la parola in maniera pulita
            raise ValueError("Il titolo del film non può essere vuoto.")
        if not isinstance(durata, str) or not durata.strip():
            raise ValueError("La durata del film non può essere vuota.")

        self.titolo = titolo.strip()
        self.durata = durata.strip()

    def __str__(self):
        return f"'{self.titolo}' ({self.durata})"

    def __eq__(self, other):
        """Permette il confronto tra oggetti Film basato su titolo e durata."""
        if not isinstance(other, Film):
            return NotImplemented
        return self.titolo == other.titolo and self.durata == other.durata

    def __hash__(self):
        """Rende gli oggetti Film hashable, utile per set/dizionari."""
        return hash((self.titolo, self.durata))


class Sala:
    """
    Rappresenta una sala con numero identificativo, film in programmazione,
    posti totali e posti prenotati.
    """
    def __init__(self, numero: int, film: Film, posti_totali: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("Il numero della sala deve essere un intero positivo.")
        if not isinstance(film, Film):
            raise TypeError("L'oggetto film deve essere un'istanza della classe Film.")
        if not isinstance(posti_totali, int) or posti_totali <= 0:
            raise ValueError("I posti totali devono essere un intero positivo.")

        self.numero = numero
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti: int) -> str:
        """
        Prenota un certo numero di posti nella sala, se disponibili.
        Restituisce un messaggio di conferma o di errore.
        """
        if not isinstance(num_posti, int) or num_posti <= 0:
            return "Errore: Il numero di posti da prenotare deve essere un intero positivo."

        posti_disponibili = self.posti_disponibili()
        if num_posti <= posti_disponibili:
            self.posti_prenotati += num_posti
            return (f"Prenotazione effettuata con successo: {num_posti} posti per "
                    f"'{self.film.titolo}' nella Sala {self.numero}.")
        else:
            return (f"Spiacente, non ci sono abbastanza posti disponibili. "
                    f"Posti disponibili: {posti_disponibili}.")

    def posti_disponibili(self) -> int:
        """
        Restituisce il numero di posti ancora disponibili nella sala.
        """
        return self.posti_totali - self.posti_prenotati

    def __str__(self):
        return (f"Sala {self.numero}: Film {self.film}, "
                f"Posti totali: {self.posti_totali}, "
                f"Posti disponibili: {self.posti_disponibili()}")


class Cinema:
    """
    Gestisce le operazioni legate alla gestione delle sale.
    """
    def __init__(self):
        self.sale = {} # Dizionario: {numero_sala: oggetto_sala}

    def aggiungi_sala(self, sala: Sala) -> str:
        """
        Aggiunge una nuova sala al cinema.
        Restituisce un messaggio di stato.
        """
        if not isinstance(sala, Sala):
            return "Errore: L'oggetto sala deve essere un'istanza della classe Sala."
        if sala.numero in self.sale:
            return f"Errore: La Sala {sala.numero} esiste già."
        
        self.sale[sala.numero] = sala
        return f"Sala {sala.numero} aggiunta con successo per il film '{sala.film.titolo}'."

    def mostra_film_disponibili(self):
        """
        Mostra tutti i film in programmazione e i posti disponibili per ogni sala.
        """
        if not self.sale:
            print("Nessuna sala configurata nel cinema.")
            return

        print("\n--- Film attualmente in programmazione ---")
        for numero_sala, sala in self.sale.items():
            print(f"Sala {numero_sala}:")
            print(f" Film: {sala.film}")
            print(f" Posti disponibili: {sala.posti_disponibili()}/{sala.posti_totali}")
        print("------------------------------------------")

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        """
        Trova il film desiderato e tenta di prenotare posti.
        Restituisce un messaggio di stato.
        """
        if not isinstance(titolo_film, str) or not titolo_film.strip():
            return "Errore: Il titolo del film non può essere vuoto."
        if not isinstance(num_posti, int) or num_posti <= 0:
            return "Errore: Il numero di posti da prenotare deve essere un intero positivo."

        found_film = False
        messages = []
        for sala in self.sale.values():
            if sala.film.titolo.lower() == titolo_film.lower():
                found_film = True
                message = sala.prenota_posti(num_posti)
                messages.append(f"Sala {sala.numero}: {message}")
        
        if not found_film:
            return f"Spiacente, il film '{titolo_film}' non è attualmente in programmazione."
        elif len(messages) == 1:
            return messages[0] # Se il film è in una sola sala, restituisci solo quel messaggio
        else:
            return "\n".join(messages) # Se il film è in più sale (anche se non richiesto esplicitamente, è una buona gestione) #.join è come una colla unisce tutte 
        #le parole togliendo virgole, virgolette, parentesi quadra ecc.. es["cane", "gatto", "mucca"] con .join diventa "cane gatto mucca"

# Creazione di alcuni film
film1 = Film("Dune - Parte Due", "2h 46m")
film2 = Film("Kung Fu Panda 4", "1h 34m")
film3 = Film("Oppenheimer", "3h 00m")

# Creazione delle sale
sala1 = Sala(1, film1, 100) # Sala 1 con Dune, 100 posti
sala2 = Sala(2, film2, 50) # Sala 2 con Kung Fu Panda, 50 posti
sala3 = Sala(3, film1, 75) # Sala 3 con Dune, 75 posti (Dune è anche in Sala 1)

# Creazione del cinema
mio_cinema = Cinema()

# Aggiunta delle sale al cinema
print(mio_cinema.aggiungi_sala(sala1))
print(mio_cinema.aggiungi_sala(sala2))
print(mio_cinema.aggiungi_sala(sala3))
print(mio_cinema.aggiungi_sala(Sala(1, film3, 80))) # Tenta di aggiungere una sala esistente
print("-" * 30)

# Mostra i film disponibili
mio_cinema.mostra_film_disponibili()
print("-" * 30)

# Tentativi di prenotazione
print("--- Tentativi di Prenotazione ---")
print(mio_cinema.prenota_film("Dune - Parte Due", 10)) # Prenota 10 posti per Dune (nella prima sala trovata)
print(mio_cinema.prenota_film("Kung Fu Panda 4", 25)) # Prenota 25 posti per Kung Fu Panda
print(mio_cinema.prenota_film("Oppenheimer", 5)) # Film non in programmazione
print(mio_cinema.prenota_film("Dune - Parte Due", 120)) # Troppi posti per una sala
print(mio_cinema.prenota_film("Kung Fu Panda 4", 30)) # Dovrebbe superare la capacità rimanente (25 già prenotati)
print("-" * 30)

# Mostra i film disponibili dopo le prenotazioni
mio_cinema.mostra_film_disponibili()
print("-" * 30)

# Test per l'uguaglianza dei Film (per la parte concettuale)
print("\n--- Test Uguaglianza Film ---")
film_test1 = Film("Avatar", "3h")
film_test2 = Film("Avatar", "3h")
film_test3 = Film("Avatar 2", "3h 12m")

print(f"Film test1: {film_test1}")
print(f"Film test2: {film_test2}")
print(f"Film test3: {film_test3}")

print(f"film_test1 == film_test2: {film_test1 == film_test2}") # True
print(f"film_test1 == film_test3: {film_test1 == film_test3}") # False

# Test con set di Film
film_set = set()
film_set.add(film_test1)
film_set.add(film_test2) # Non dovrebbe essere aggiunto perché è uguale a film_test1
film_set.add(film_test3)
film_set.add(Film("Dune - Parte Due", "2h 46m")) # film1 già creato sopra

print(f"Numero di film unici nel set: {len(film_set)}") # Dovrebbe essere 3
for f in film_set:
    print(f" - {f}")
print("-" * 30)

# Esempio di gestione degli errori di input
try:
    Film("", "1h")
except ValueError as e:
    print(f"Errore nella creazione del film: {e}")

try:
    Sala(0, film1, 100)
except ValueError as e:
    print(f"Errore nella creazione della sala: {e}")

try:
    sala1.prenota_posti(0)
except ValueError as e: # Questo non sarà catturato perché ho messo un return stringa nell'implementazione
    print(f"Errore nella prenotazione: {e}")

	
