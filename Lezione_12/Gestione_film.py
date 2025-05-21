class MovieCatalog:
    def __init__(self) -> None:
        self.setCatalog()
        #metodi getter
        '''metodo che ritorna il valore dell'attributo self.catalog'''
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
        #metodo setter
        '''metodo che che consente di inizializzare l'attributo self.catalog'''
    def setCatalog(self) -> None:
        self.catalog: dict[str, list[str]] = {}
        '''metodo per visualizzare i dettagli di un catalogo'''
    def __str__(self) -> str:
        string:str = "Catalog"
        if self.catalog:
            for key, values in self.catalog.items():
                temp_string: str = "\n" + str(key) + ": " + str(values)
                string = string + temp_string
                return string
    def add_movies(self, director_name: str, movies: list[str]) -> None:
        if not director_name:
            print("il regista non è valido")
        elif not movies:
            print("la lista dei film non puè essere vuota")
        else:
            if director_name in self.catalog:
                for movie in movies:
                    if movie in self.catalog[director_name]:
                        print("il film movie è gia presente nel catalogo")
                    else:
                        self.catalog[director_name].append(movie)
            else:
                self.catalog[director_name] = movies

    def remove_movie(self, director_name: str, movie: str) -> None:
        if not director_name:
            print("il regista non è valido")
        elif not movie:
            print("il film non è valido")
        else:
            if director_name in self.catalog and movie in self.catalog[director_name]:
                self.catalog[director_name].remove(movie)
            if not self.catalog[director_name]:
                del self.catalog[director_name]

    def list_director(self) -> list[str] | str:
        if self.catalog:
            return list(self.catalog.keys())
        else:
            return f"non ci sono registi nel catalog, perche il catalogo è vuoto"
        
    def get_movies_by_director(self, director_name) -> list[str] | str:
        if not director_name:
            return("il regista non è valido")
        else:
            if director_name in self.catalog:
                return self.catalog[director_name]
            else:
                return f"il regista {director_name} non è nel catalogo"
