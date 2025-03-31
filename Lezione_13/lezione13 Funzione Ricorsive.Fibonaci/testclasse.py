def find_element(lst: list, element: int) ->bool:
    for item in lst:
        if item == element:
            return True
    return False
print(find_element([1], 4))


'''def list_statistics(numeri: list[int]) -> tuple[int, int, float]:
    if not numeri:
        return(0, 0, 0, 0)
    massimo = max(numeri)
    minimo = min(numeri)
    media = sum(numeri) / len(numeri)

    return (massimo, minimo, media)
numeri = [1, 2, 3, 4, 5]
risultato = list_statistics(numeri)
print(risultato)'''

'''def is_magic_number(n):
    return '7' in str(n)
print(is_magic_number(714))
print(is_magic_number(123))'''

'''def ruota_lista_sinistra(lista, k):
    lunghezza = len(lista)
    if lunghezza == 0:
        return []
    k = k % lunghezza
    lista_ruotata = lista[k:] + lista[:k]
    return lista_ruotata'''

'''def remove_duplicates(lista):
    elementi_unici = []
    for elemento in lista:
        if elemento not in elementi_unici:
            elementi_unici.append(elemento)
    return elementi_unici'''


'''def rounded_average(list):
    if not list:
        return 0
    average = sum(list) / len(list)
    return round(average)
    '''

'''def check_parentheses(stringa):
    stack = []
    for carratere in stringa:
        if carratere == '(':
            stack.append(carratere)
        elif carratere == ')':
            if not stack:
                return False
            stack.pop()
    return not stack'''

'''def count_isolated(lst: list[int]) -> int:
    count = 0
    for i in range(len(lst)):
        if (i == 0 or lst[i] != lst[i-1]) and (i == len(lst) - 1 or lst[i] != lst[i + 1]):
            count += 1
    return count'''