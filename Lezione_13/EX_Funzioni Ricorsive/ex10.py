def charDuplicator(stringa):
    if not stringa:
        return ""
    else:
        return stringa[0] + stringa[0] + charDuplicator(stringa[1:])
    
stringa_originale = "libro"
risultato = charDuplicator(stringa_originale)
print(risultato)  #OP:  lliibbrroo