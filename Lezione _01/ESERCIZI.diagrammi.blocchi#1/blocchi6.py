#CALCOLO DEL FATTORIALE DI UN NUMERO
n = int(input("Inserire un numero intero:  "))
if n <= 0:
    print("Il numero deve essere positivo")
else:
    fattoriale = 1
    i = 1
    while i <= n:
        fattoriale = fattoriale * i
        i = i + 1
    print("Il fattoriale di", n, "è:", fattoriale)

    #ESEMPIO FATTIRIALE DI 5 È: 5*4*3*2*1 = 120