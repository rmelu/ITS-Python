class MathOperations:
    """
    Una classe per raggruppare operazioni matematiche di base.
    Contiene metodi statici per addizione e moltiplicazione.
    """

    @staticmethod
    def add(num1, num2):
        """
        Calcola la somma di due numeri.

        Args:
            num1 (int or float): Il primo numero.
            num2 (int or float): Il secondo numero.

        Returns:
            int or float: La somma di num1 e num2.
        """
        # Puoi aggiungere qui una validazione dell'input se necessario
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Entrambi gli input devono essere numerici.")
        return num1 + num2

    @staticmethod
    def multiply(num1, num2):
        """
        Calcola il prodotto di due numeri.

        Args:
            num1 (int or float): Il primo numero.
            num2 (int or float): Il secondo numero.

        Returns:
            int or float: Il prodotto di num1 e num2.
        """
        # Puoi aggiungere qui una validazione dell'input se necessario
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Entrambi gli input devono essere numerici.")
        return num1 * num2

if __name__ == "__main__":
    print("--- Test della classe MathOperations ---")

    # Test del metodo statico add
    print("\nTest del metodo add():")
    result_add1 = MathOperations.add(5, 3)
    print(f"5 + 3 = {result_add1}")  # Output atteso: 8

    result_add2 = MathOperations.add(-10, 20.5)
    print(f"-10 + 20.5 = {result_add2}")  # Output atteso: 10.5

    # Test del metodo statico multiply
    print("\nTest del metodo multiply():")
    result_mult1 = MathOperations.multiply(4, 7)
    print(f"4 * 7 = {result_mult1}")  # Output atteso: 28

    result_mult2 = MathOperations.multiply(2.5, -3)
    print(f"2.5 * -3 = {result_mult2}")  # Output atteso: -7.5

    # Dimostrazione che i metodi statici possono essere chiamati anche tramite un'istanza (ma è sconsigliato)
    # math_obj = MathOperations()
    # print(f"\nChiamata tramite istanza (sconsigliata):")
    # print(f"10 + 5 = {math_obj.add(10, 5)}")

    # Test con input non numerici (per dimostrare la validazione)
    print("\nTest con input non numerici (dovrebbe generare un errore):")
    try:
        MathOperations.add("hello", 5)
    except TypeError as e:
        print(f"Errore: {e}")

    try:
        MathOperations.multiply(10, [1, 2])
    except TypeError as e:
        print(f"Errore: {e}")