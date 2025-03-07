name:list = ['Matteo','Francesco','Marco','Carlo','Alan','Franco']
mess:list = ["Mi dispiace posso invitare solo due persone a cena"]
name.pop()
name.pop()
name.pop()
name.pop()
name.insert(len(name)//2, "Codoaldo")
name.append("Einaudi")
for i in range (len(name)):
    print(name[i],mess[0])
print("Purtroppo il mio tavolo da pranzo non arrivera a cena")