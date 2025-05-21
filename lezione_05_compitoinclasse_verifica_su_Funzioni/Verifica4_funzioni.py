def find_disappeared_numbers(nums):
    n = len(nums)
    numeri_mancanti = []
    numeri_presenti = set(nums)

    for i in range(1, n + 1):
        if i not in numeri_presenti:
            numeri_mancanti.append(i)
    return numeri_mancanti
