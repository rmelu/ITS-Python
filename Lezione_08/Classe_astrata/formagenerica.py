from abc import ABC, abstractmethod

class Formagenerica(ABC):

    @abstractmethod
    def draw(self) -> None: #draw non restituisce niente
        pass
    
    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore! Shape non può essere una stringa vuota")

    def getShape(self) -> str:
        return self.shape