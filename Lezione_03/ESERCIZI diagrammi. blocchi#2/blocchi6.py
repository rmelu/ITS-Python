x = int(input("inserisci un valore per x: "))
if x <= 0:
    print("Errore, x deve essere positivo.")
else:
    i = 0
    sum = 0
    while i < 10:
        n = int(input("inserisci un valore per n: "))
        if x % 2 == 0:  #verifichiamo se x è pari
            if n < x:
                sum += n
        else:   #x è dispari
            if n > x / 2:
                sum =+ n
        i = i + 1
    print("somma:", sum)
