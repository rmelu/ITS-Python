n = int(input("inserisci un numero intero positivo: "))
if n % 1 != 0 or n <= 0:
    print("Errore, n deve essere positivo. ")
else:
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i * i
        i += 1
        print(sum)
    