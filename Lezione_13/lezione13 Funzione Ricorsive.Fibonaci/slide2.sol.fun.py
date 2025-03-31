def countdown (n:int) -> None:
    #n is positive (n >= 0)
    if n >= 0:
        while n >=0:
            print(n)
        n = n -1
    else:
        print("errore il numero inserito è negativo ")
countdown(-5)        
countdown(-2)