città = ["Roma","Milano","Firenze","Venezia","Napoli"]
print("lista originale:", città)
città.append("Torino")
print("lista con nuova città:", città)
città.insert(0, "Bologna")
print("lista con città inserita all'inizio:", città)
città.pop()
print("lista con ultima città rimossa:", città)
città.remove("Firenze")
print("lista con città specifica rimossa:", città)
città.sort()
print("lista ordinata alfabeticamente:", città)
città.sort(reverse=True)
print("lista ordinata alfabeticamente al contrario:", città)
città.reverse()
print("lista con ordine invertito:", città)
lunghezza = len(città)
print("lunghezza della lista:", lunghezza)
prima_città = città[0]
print("prima città della lista:", prima_città)
città[1] = "Genova"
print("lista con elemento sostituito:", città)
sotto_lista = città[1:4]
print("sotto_lista:", sotto_lista)
altre_città = ["palermo","catania"]
città.extend("altre_citta")
print("lista estesa:", città)
città.clear()
print("lista vuota:", città)
