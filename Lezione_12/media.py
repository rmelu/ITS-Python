class Media:

    def __init__(self, title: str, year: int) -> None:
        self.setTitle(title)
        self.setYear(year)

    def setTitle(self, title: str) -> None:
        if title:
            self.title = title
        else: 
            print("Errore")

    def setYear(self, year: int) -> None:
        if year > 1000:
            self.year = year
        else:
            print("Errore")

    def getTitle(self) -> str:
        return self.title
    
    def getYear(self) -> int:
        return self.year

    def __str__(self) -> str:
        return f"Titolo: {self.getTitle()}\nAnno: {self.getYear()}"