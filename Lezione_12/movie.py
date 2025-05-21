from media import Media

class Movie(Media):

    def __init__(self, title: str, year: int, durata: int) -> None:
        #inisializzare la suepr classe richiamando il metodo __init__ della super classe Media
         super().__init__(title, year)
         self.setDurata(durata)

    def setDurata(self, durata: int) -> None:
        if durata >= 0:
            self.durata = durata
        else:
            print("errore")

    def getDurata(self) -> int:
        return self.durata
    
    def __str__(self) -> int:
        return f"{super.__str__()}\nDurata: {self.getDurata()}"

