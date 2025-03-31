for i in range(5):
    while True:
        numero = input(f"Inserisci il {i + 1}° numero (tra 1 e 30): ")
        #Verifica se l'output è un numero intero
        if numero.replace(".", "", 1).isdigit(): #Verifica se è un numero (anche con decimali) 
            numero = float(numero)   #Converti in float per il controllo dell?interezza
            if numero.is_integer():   #Verifica se è intero
                numero = int(numero)  #Converti in dietro
                if 1 <= numero <= 30:
                    break                #Esci dal ciclo se il numero è valido
                else:
                    print("Il numero deve essere compreso tra 1 e 30.")
            else:
                print("Il numero deve essere  intero.")
        else:
            print("Input non valido. inserisci un numero.")
    #Stampa la riga con gli asterischi
    print("*" * numero)





#replace serve per sostituire una o piu occorenzze di una sottostringa con un altra sottostringa.
#esempio
'''stringa = "Hello World!"
nuova_stringa = stringa_replace("world", "Python")
print(nuova_stringa)  #Output: Hello, Python!'''