def sum_primary_diagonali(matrix):
    n = len(matrix)
    return sum(matrix[i][n - 1 - i] for i in range(n))
def somma_diagonali_matrice(matrix):
    """
    Calcola la somma degli elementi della diagonale principale e della diagonale secondaria di una matrice quadrata.

    Args:
        matrix (list of list of int): La matrice quadrata.

    Returns:
        int: La somma degli elementi delle due diagonali.
    """
    n = len(matrix)
    somma_diagonali = 0

    for i in range(n):
        somma_diagonali += matrix[i][i]  # Diagonale principale
        somma_diagonali += matrix[i][n - 1 - i]  # Diagonale secondaria

    return somma_diagonali
if __name__ == "__main__":
    # Esempio di utilizzo
    matrice = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(somma_diagonali_matrice(matrice))  # Output: 30
    print(sum_primary_diagonali(matrice))  # Output: 15
    matrice2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
