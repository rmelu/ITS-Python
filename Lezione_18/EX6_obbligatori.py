from math import gcd

# === Eccezioni personalizzate ===
class ErroreFrazione(Exception):
    """Eccezione base per errori nella gestione delle frazioni."""
    pass

class DenominatoreZeroError(ErroreFrazione):
    """Errore sollevato quando il denominatore è zero."""
    def __init__(self):
        super().__init__("Il denominatore non può essere zero.")

class OperazioneNonValidaError(ErroreFrazione):
    """Errore sollevato per operazioni non valide tra frazioni."""
    def __init__(self, messaggio:str):
        super().__init__(f"Operazione non valida: {messaggio}")

# === Funzioni principali ===
def crea_frazione(numeratore:int, denominatore:int) -> tuple[int, int]:
    """
    Crea una frazione e la semplifica.
    Solleva un errore se il denominatore è zero.
    """
    try:
        if denominatore == 0:
            raise DenominatoreZeroError()
        return semplifica_frazione((numeratore, denominatore))
    except DenominatoreZeroError as e:
        raise e
    except Exception as e:
        raise ErroreFrazione(f"Errore durante la creazione della frazione: {e}")

def semplifica_frazione(frazione:tuple[int, int]) -> tuple[int, int]:
    """
    Semplifica la frazione usando il massimo comune divisore.
    """
    try:
        num:int = frazione[0]
        den:int = frazione[1]
        comune:int = gcd(num, den)
        num //= comune
        den //= comune

        # Normalizza il segno (il segno va sempre al numeratore)
        if den < 0:
            num *= -1
            den *= -1

        return (num, den)
    except Exception as e:
        raise ErroreFrazione(f"Errore durante la semplificazione: {e}")

def somma_frazioni(f1:tuple[int, int], f2:tuple[int, int]) -> tuple[int, int]:
    """Somma due frazioni e ritorna il risultato semplificato."""
    try:
        num:int = f1[0] * f2[1] + f2[0] * f1[1]
        den:int = f1[1] * f2[1]
        return semplifica_frazione((num, den))
    except Exception as e:
        raise OperazioneNonValidaError(f"Errore nella somma: {e}")

def sottrai_frazioni(f1:tuple[int, int], f2:tuple[int, int]) -> tuple[int, int]:
    """Sottrae la seconda frazione dalla prima."""
    try:
        num:int = f1[0] * f2[1] - f2[0] * f1[1]
        den:int = f1[1] * f2[1]
        return semplifica_frazione((num, den))
    except Exception as e:
        raise OperazioneNonValidaError(f"Errore nella sottrazione: {e}")

def moltiplica_frazioni(f1:tuple[int, int], f2:tuple[int, int]) -> tuple[int, int]:
    """Moltiplica due frazioni e ritorna il risultato semplificato."""
    try:
        num:int = f1[0] * f2[0]
        den:int = f1[1] * f2[1]
        return semplifica_frazione((num, den))
    except Exception as e:
        raise OperazioneNonValidaError(f"Errore nella moltiplicazione: {e}")

def dividi_frazioni(f1:tuple[int, int], f2:tuple[int, int]) -> tuple[int, int]:
    """Divide la prima frazione per la seconda."""
    try:
        if f2[0] == 0:
            raise DenominatoreZeroError()
        num:int = f1[0] * f2[1]
        den:int = f1[1] * f2[0]
        return semplifica_frazione((num, den))
    except DenominatoreZeroError as e:
        raise e
    except Exception as e:
        raise OperazioneNonValidaError(f"Errore nella divisione: {e}")

def frazioni_equivalenti(f1:tuple[int, int], f2:tuple[int, int]) -> bool:
    """Verifica se due frazioni sono equivalenti."""
    try:
        return f1[0] * f2[1] == f2[0] * f1[1]
    except Exception as e:
        raise OperazioneNonValidaError(f"Errore nel controllo di equivalenza: {e}")
    
# === Test ===
try:
    f1 = crea_frazione(3, 6)
    f2 = crea_frazione(1, 2)

    print("Frazione 1:", f1)  # (1, 2)
    print("Frazione 2:", f2)  # (1, 2)
    print("Sono equivalenti?", frazioni_equivalenti(f1, f2))  # True

    somma = somma_frazioni(f1, f2)
    print("Somma:", somma)  # (1, 1)

    divisione = dividi_frazioni(f1, f2)
    print("Divisione:", divisione)  # (1, 1)

except ErroreFrazione as errore:
    print("Si è verificato un errore:", errore)