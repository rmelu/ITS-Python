from datetime import datetime, date
from typing import Any

# Classe per rappresentare una singola data
class Data:
    def __init__(self, data_str:str) -> None:
        # Converte una stringa 'gg.mm.aaaa' in un oggetto datetime.date
        try:
            self.data:date = datetime.strptime(data_str, "%d.%m.%Y").date()
        except ValueError:
            # Se il formato non è corretto, solleva un'eccezione
            raise ValueError(f"Formato data non valido: {data_str}. Usa 'gg.mm.aaaa'.")

    def __str__(self) -> str:
        # Restituisce la data in formato 'gg.mm.aaaa' quando l'oggetto viene stampato
        return self.data.strftime("%d.%m.%Y")

    def __eq__(self, other:Any) -> bool:
        # Permette di confrontare due oggetti Data tra loro
        if isinstance(other, Data) and self.data == other.data:
            return True   
        else:
            return False


# Classe per gestire una lista di oggetti Data
class GestoreDate:
    def __init__(self) -> None:
        # Inizializza una lista vuota di date
        self.date:list[Data] = []

    def aggiungi_data(self, data_str: str) -> None:
        # Aggiunge una nuova data alla lista
        nuova_data:Data = Data(data_str)
        self.date.append(nuova_data)

    def elimina_data(self, data_str: str) -> None:
        # Elimina una data esistente dalla lista, se presente
        data_da_eliminare:Data = Data(data_str)
        if data_da_eliminare in self.date:
            self.date.remove(data_da_eliminare)
        else:
            print("Data non trovata per l'eliminazione.")

    def modifica_data(self, vecchia_data_str: str, nuova_data_str: str) -> None:
        # Sostituisce una data esistente con una nuova
        vecchia_data:Data = Data(vecchia_data_str)
        nuova_data:Data = Data(nuova_data_str)
        if vecchia_data in self.date:
            indice:int = self.date.index(vecchia_data)
            self.date[indice] = nuova_data
        else:
            print("Data da modificare non trovata.")

    def cerca_data(self, data_str: str) -> bool:
        # Restituisce True se la data è presente nella lista
        data_cercata:Data = Data(data_str)
        return data_cercata in self.date

    def mostra_date(self) -> list[str]:
        # Restituisce una lista di stringhe rappresentanti le date
        return [str(d) for d in self.date]



gestore:GestoreDate = GestoreDate()                              # Crea un nuovo gestore
gestore.aggiungi_data("11.04.2025")                                # Aggiunge la data 11 aprile 2025
gestore.aggiungi_data("01.01.2024")                                # Aggiunge la data 1 gennaio 2024
gestore.modifica_data("01.01.2024", "02.01.2024")                  # Modifica la seconda data
gestore.elimina_data("11.04.2025")                                 # Elimina la prima data

# Visualizzazione dei risultati
print("Date attuali:", gestore.mostra_date())                      # Stampa tutte le date memorizzate
print("La data 02.01.2024 è presente?")
print(gestore.cerca_data("02.01.2024"))  # Verifica presenza