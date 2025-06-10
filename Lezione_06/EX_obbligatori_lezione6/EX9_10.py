class Ristorante:
    """Modella un ristorante."""

    def __init__(self, nome_ristorante, tipo_cucina):
        """Inizializza gli attributi del ristorante."""
        self.nome_ristorante = nome_ristorante
        self.tipo_cucina = tipo_cucina
        self.clienti_serviti = 0 # Un attributo per l'esercizio 9-4, per esempio

    def descrivi_ristorante(self):
        """Stampa il nome e il tipo di cucina del ristorante."""
        print(f"Il ristorante si chiama {self.nome_ristorante}.")
        print(f"Offre cucina {self.tipo_cucina}.")

    def apri_ristorante(self):
        """Stampa un messaggio che indica che il ristorante è aperto."""
        print(f"{self.nome_ristorante} è ora aperto!")

    def imposta_clienti_serviti(self, numero):
        """Imposta il numero totale di clienti serviti."""
        self.clienti_serviti = numero

    def incrementa_clienti_serviti(self, incremento):
        """Incrementa il numero di clienti serviti."""
        self.clienti_serviti += incremento