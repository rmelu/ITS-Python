from string import ascii_lowercase, ascii_uppercase
def frequenza_di_parole_uniche_con_Normalizzazione(messaggio):
    """
    Calcola la frequenza delle parole uniche in un messaggio normalizzato.
    :param messaggio: il messaggio da analizzare
    :return: un dizionario con le parole uniche e le loro frequenze
    """
    # Normalizza il messaggio: rimuove la punteggiatura e converte in minuscolo
    normalizzato = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in messaggio)
    
    # Divide il messaggio in parole
    parole = normalizzato.split()
    
    # Conta le frequenze delle parole
    frequenze = {}
    for parola in parole:
        if parola in frequenze:
            frequenze[parola] += 1
        else:
            frequenze[parola] = 1
            
    return frequenze

print(frequenza_di_parole_uniche_con_Normalizzazione("Ciao mondo! Ciao a tutti. Mondo, come va?"))
# Output: {'ciao': 2, 'mondo': 2, 'a': 1, 'tutti': 1, 'come': 1, 'va': 1}
# Example usage
