def convert_lista_of_tuple(list_1: list[tuple]) -> dict:
    dict_1: dict = {}
    for element in list_1:
        key, value = element[0], element[1]
        if key in dict_1:
            dict_1[key] += value
        else:
            dict_1[key] = value
        return dict_1
lista_1: list[tuple] =[(0, "valore"), (1, "valore2")]
dict_2: dict = convert_lista_of_tuple(list_1 = lista_1)

print(dict_2)