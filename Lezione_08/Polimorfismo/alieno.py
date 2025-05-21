class Alieno:
    #di un alieno ci interessa la galassia di provenienza
    #self.galaxy: str

    #inizializzare un oggetto della classe Alieno

    def __init__(self, galaxy: str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy: str) ->str:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("ERRORE La galassia di provenienza non può essere la stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("lkgfhlaeurlginejògu4")
    
    def __str__(self) -> str:
        return (f"\nalieno proveniente dalla galasia{self.Galaxy()}")