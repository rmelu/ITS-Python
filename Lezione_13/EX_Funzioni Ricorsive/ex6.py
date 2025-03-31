def fattori(n: int)-> int:
    if n == 1:  # n poitrebbe diventare anche 1 o due (2 **3) * (1 **3)
        return 1
    else:
        return (n **3) *fattori(n - 1) # 2 **3   1 - 1
print(fattori(4))
print(fattori(10))
print(fattori(2))

# in caso di 4 sarebbe (4 * 4* 4)  = 64
                    #    (3 * 3* 3) = 27
                    #    ( 2 * 2 * 2) = 8
                    #   (1 * 1* 1) = 1
                    # totale  13. 824

