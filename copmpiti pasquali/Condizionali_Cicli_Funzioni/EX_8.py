def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
    ore_da_mezzanotte = ore if ore != 12 else 12
    return (ore_da_mezzanotte * 3600) + (minuti * 60) + secondi

def time_difference(ore1: int, minuti1: int, secondi1: int, ore2: int, minuti2: int, secondi2: int) -> int:
    secondi_totali1 = seconds_since_noon(ore1, minuti1, secondi1)
    secondi_totali2 = seconds_since_noon(ore2, minuti2, secondi2)
    differenza =  secondi_totali2 - secondi_totali1
    return differenza
print(time_difference(1, 0, 0, 3, 15, 30))
print(time_difference(11, 59, 59, 2, 0, 0))
print(time_difference(0, 0, 0, 12, 0, 0))
print(time_difference(9, 0, 0, 11, 0, 0))