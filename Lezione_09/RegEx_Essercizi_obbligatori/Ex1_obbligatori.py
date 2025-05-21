import re
def riconosce_intero_positivo(stringa):
    #riconosci se una stringa rappresenta un numero intero positivo .
    #Args: la stringa da annalizzare
    #returns: 
            #True se la stringa è un numero intero positivo, False altrimenti.
            pattern =  r"^[1-9]\d*$"
            return bool(re.fullmatch(pattern, stringa))
print(riconosce_intero_positivo("123"))
print(riconosce_intero_positivo("98756"))
print(riconosce_intero_positivo("abc"))
print(riconosce_intero_positivo(""))
print(riconosce_intero_positivo("-123"))
print(riconosce_intero_positivo("12.3"))         
