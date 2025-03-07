'''#ES- 1.1
x = float(input("verifica approssimazione(x)"))
funzione_con_lista: x("il numero in virgola mobile da testare")

#calcolare 1/x
y = 1.0 / x #vizzualizare i valori e il prodotto 
print(f"x = {x}")
print(f"y = {y}")
print(f"x * y = {x * y}")
#sottrai dal risultato e visualiza
risultato = x * y - x
print(f"x * y - x = {risultato}")
if risultato == 0:
    print("perfetto")
else:
    print("no buono")
'''
#ES 1-2
X : float = float(input("inserire numero con virgola"))
y : int = X%2.0
print(f"i valori di X e Y sono {X} {y}")