import random
def mossa_tartaruga():
    #calcola la mossa della tattaruga
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3     #passo veloce
    elif 6 <= i <= 7:
        return -6    #scivolta
    else:
        return 1  #passo lento
    
def mossa_lepre():
    #calcola la mossa delle lepre
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        return 0      #riposo
    elif 3 <= i <= 4:
        return 9    #grande balzo
    elif i == 5:
        return -12  #grande scivolata
    elif 6 <= i <= 8:
        return 1  #piccolo balzo
    else:
        return -2  #piccola scivolata
    
def visualizza_corsa(tartaruga_pos, lepre_pos):
    #visualizza la corsa sulla corsia
    corsa = ['_'] * 70
    if tartaruga_pos == lepre_pos:
        corsa[tartaruga_pos - 1] = 'OUCH!!!'
    else:
        corsa[tartaruga_pos - 1] = 'T'
        corsa[lepre_pos - 1] = 'H'
    print(''.join(corsa))

#simula la gara tra la tarttaruga e la lepre.
tartaruga_pos = 1
lepre_pos = 1
print("BANG !!!!!! AND THEY'RE OFF !!!!!")

while tartaruga_pos < 70 and lepre_pos <  70:
    tartaruga_pos = max(1, tartaruga_pos + mossa_tartaruga())
    lepre_pos = max(1, lepre_pos + mossa_lepre())
    visualizza_corsa(tartaruga_pos, lepre_pos)

if tartaruga_pos >= 70 and lepre_pos >= 70:
        print("IT'S A TIE")
elif tartaruga_pos >= 70:
        print("TOUTOISE WINS || VAY !!!!")
else:
        print("HARE WINS || YUCH!!!")

