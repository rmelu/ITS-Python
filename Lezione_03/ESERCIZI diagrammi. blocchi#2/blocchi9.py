n = int(input("Inserisci unnumero intero: "))

if n <= 0:
    print("n deve essere intero o positivo ")
else:
    cont = 0
    i = 0
    while i < 10:
        x = int(input("Inserisci un numero intero: "))
        if x % n == 0:
            cont = cont + 1
        i = i + 1
    print(cont)