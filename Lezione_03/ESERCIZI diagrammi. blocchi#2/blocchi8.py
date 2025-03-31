A = int(input("Inserisci il valore di A: "))
B =  int(input("Inserisci il valore di B: "))
#verificare se A è minore di B
if A >= B:
    print("A deve essere minore di B")
else: #verificare se A e B sono positivi
    if A <= 0 or B <= 0:
        print("A e B devono essere positivi")
    else: # verificare se A e B sono interi
        if A % 1 != 0 or B % 1 != 0:
            print("A e B devono essere interi")
        else:
            somma = 0
            i = A
            while i <= B:
                somma += i
                i += 1
            print(somma)

