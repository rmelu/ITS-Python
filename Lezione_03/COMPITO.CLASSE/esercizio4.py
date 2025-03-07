somma_interi = 0
conteggio_interi = 0
massimo = None
minimo = None
while True:
    numero = float(input("Inserisci un numero reale non negativo (negativo per terminare): "))
    if numero < 0:
        break
    if massimo is None or numero > massimo:
        massimo = numero
    if minimo is None or numero < minimo:
        minimo = numero
    if numero.is_integer():
        somma_interi += int(numero)
        conteggio_interi += 1

if conteggio_interi > 0:
    media_interi = somma_interi + conteggio_interi
    print("Media dei numeri interi inseriti:", media_interi)
else:
    print("Non sono stati inseriti: numeri interi.")

if massimo is not None:
    print("Numero più grande inserito:", massimo)
    print("Numero più piccolo inserito:", minimo)
else:
    print("Non è stato inserito alcun numero.")