
import time

class Timer:
    def __init__(self):
        """
        Inizializza il timer.
        """
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def __enter__(self):
        """
        Metodo chiamato all'ingresso del blocco 'with'.
        Registra il tempo di inizio.
        """
        self.start_time = time.perf_counter()
        return self # Il context manager non restituisce un oggetto file, ma l'istanza stessa del Timer

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Metodo chiamato all'uscita del blocco 'with'.
        Calcola e stampa il tempo trascorso.

        Args:
            exc_type: Il tipo di eccezione se un'eccezione si è verificata.
            exc_val: Il valore dell'eccezione.
            exc_tb: Il traceback dell'eccezione.
        """
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Tempo trascorso: {self.elapsed_time:.5f} secondi")

        # Se non vogliamo sopprimere le eccezioni, restituiamo None (o non restituiamo nulla)
        # return False # Equivalente a non ritornare nulla, l'eccezione si propaga

	
