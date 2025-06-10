'''from abc import ABC, abstractmethod

class Shape(ABC):

    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass'''


import abc
import math

# Definizione della classe base astratta Shape
class Shape(abc.ABC):
    """
    Classe base astratta per le forme geometriche.
    Definisce i metodi astratti 'area' e 'perimeter'.
    """
    @abc.abstractmethod
    def area(self):
        """
        Calcola e restituisce l'area della forma.
        Questo metodo deve essere implementato dalle sottoclassi concrete.
        """
        pass

    @abc.abstractmethod
    def perimeter(self):
        """
        Calcola e restituisce il perimetro della forma.
        Questo metodo deve essere implementato dalle sottoclassi concrete.
        """
        pass

class Circle(Shape):
    """
    Rappresenta un cerchio, ereditando dalla classe astratta Shape.
    Fornisce implementazioni concrete per i metodi 'area' e 'perimeter'.
    """
    def __init__(self, radius):
        """
        Inizializza un oggetto Circle con il raggio specificato.
        """
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Il raggio deve essere un numero positivo.")
        self.radius = radius

    def area(self):
        """
        Calcola l'area del cerchio utilizzando la formula pi * r^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calcola il perimetro (circonferenza) del cerchio utilizzando la formula 2 * pi * r.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rappresenta un rettangolo, ereditando dalla classe astratta Shape.
    Fornisce implementazioni concrete per i metodi 'area' e 'perimeter'.
    """
    def __init__(self, width, height):
        """
        Inizializza un oggetto Rectangle con larghezza e altezza specificate.
        """
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("La larghezza deve essere un numero positivo.")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("L'altezza deve essere un numero positivo.")
        self.width = width
        self.height = height

    def area(self):
        """
        Calcola l'area del rettangolo utilizzando la formula larghezza * altezza.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcola il perimetro del rettangolo utilizzando la formula 2 * (larghezza + altezza).
        """
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    print("--- Test delle classi Shape ---")

    # Creazione di un'istanza di Circle
    print("\nCreazione di un Cerchio con raggio 5:")
    circle = Circle(5)
    print(f"Area del Cerchio: {circle.area():.2f}")
    print(f"Perimetro del Cerchio: {circle.perimeter():.2f}")

    # Creazione di un'istanza di Rectangle
    print("\nCreazione di un Rettangolo con larghezza 4 e altezza 6:")
    rectangle = Rectangle(4, 6)
    print(f"Area del Rettangolo: {rectangle.area():.2f}")
    print(f"Perimetro del Rettangolo: {rectangle.perimeter():.2f}")

    # Esempio di utilizzo polimorfico
    print("\nTest polimorfico:")
    shapes = [Circle(3), Rectangle(5, 10)]
    for shape in shapes:
        print(f"\nTipo di forma: {type(shape).__name__}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimetro: {shape.perimeter():.2f}")

    # Tentativo di istanziare la classe astratta (questo genererà un errore)
    # try:
    #     abstract_shape = Shape()
    # except TypeError as e:
    #     print(f"\nErrore atteso (impossibile istanziare classe astratta): {e}")