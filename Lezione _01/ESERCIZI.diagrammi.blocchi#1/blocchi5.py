#verichiamo se un numero è primo
n = int(input("Inserisci un numero "))
if n < 2:
    is_prime = False
else:
    is_prime = True
    div = 2
    while div * div <= n:
        if n % div == 0:
            is_prime = False
            break            #ESCI DAL CICLO SE TROVI UN DIVISORE
        div = + 1
if is_prime:
    print("Il numero è primo ")
else:
    print("Il numero non è primo ")