from formagenerica import Formagenerica

class Rettangolo(Formagenerica):
    def __init__(self):
        super().__init__()
        
        self.setShape('rettangolo')
        
    def draw(self) -> None:
        
        print(f"\n{self.getShape()}")
        
        # outer for
        for i in range(5):
            #inner for
            for j in range(5*2):
                 #lato a e lato d del rettangolo
                if i == 0 or i == 5-1:
                    print("*", end=" ")
                   # lato b e lato c del rettangolo
                elif j == 0 or j == (5*2)-1 :
                    print("*", end=" ")
                else:
                    print(print(" ", end=" "))
        print("\n", end="")
            



'''

def disegna_rettangolo_testuale(larghezza, altezza):
  #Disegna un rettangolo testuale con la data larghezza e altezza.
    if larghezza <= 0 or altezza <= 0:
        print("Larghezza e altezza devono essere positive.")
        return

    for riga in range(altezza):
        if riga == 0 or riga == altezza - 1:
            print("*" * larghezza)  # Bordo superiore e inferiore
        else:
            print("*" + " " * (larghezza - 2) + "*")  # Lati interni

# Esempio per un rettangolo 10x5 (come sembra nell'immagine)
larghezza_rettangolo = 10
altezza_rettangolo = 5
disegna_rettangolo_testuale(larghezza_rettangolo, altezza_rettangolo)'''
