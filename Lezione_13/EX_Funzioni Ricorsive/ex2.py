def compoundinterest(m:float, t:int) -> float:
    #t < = 0, non è passato un mese da quando ho depositato il saldo m, quindi il saldo sarà m
    if t <= 0:
        return round(m,2)
    else:
        #se t = 1, è passato un mese, saldo sul conto sarà 1.005 * m,  se m = 1000, il saldo sara 1.005 * 1000 = 1005
        #se t = 2, 1005 * 1.005 = 1010,03
        #se t = 3, 1010,03 * 1.015,08
        return round(1.005 * compoundinterest(m, t-1), 2)
    
print(compoundinterest(1000, 3))
    