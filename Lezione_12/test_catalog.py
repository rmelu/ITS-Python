from Gestione_film import MovieCatalog

catalog: MovieCatalog = MovieCatalog()

catalog.add_movies('Steven Spielberg', ['Casper', 'Ritorno al Futuro'])

catalog.add_movies('Steven Spielberg', ['ET'])

catalog.add_movies('Quentin Tarantino', ['Pulp Fuction', 'kill bill'])

catalog.remove_movie('Quentin Tarantino', 'kill Bill')

catalog.remove_movie('Quentin Tarantino', 'Pulp Fuction')


print(catalog)

print(catalog.list_director())

print(catalog.get_movies_by_director('Steven Spielberg'))




















































'''
class Movie:
    def __init__(self, title, director_name, genre):
        self.title = title
        self.director_name = director_name
        self.genre = genre

    def __str__(self):
        return f"Titolo: {self.title}, Regista: {self.director_name}, Genere: {self.genre}"

class Catalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, movie):
        if movie.genre not in self.catalog:
            self.catalog[movie.genre] = []
        self.catalog[movie.genre].append(movie)

    def get_movies_by_genre(self, genre):
        return self.catalog.get(genre, [])

    def get_movies_by_director(self, director_name):
        movies_by_director = []
        for movies in self.catalog.values():
            for movie in movies:
                if movie.director_name == director_name:
                    movies_by_director.append(movie)
        return movies_by_director

# Esempio di utilizzo
my_catalog = Catalog()
my_catalog.add_movie(Movie("Il Padrino", "Francis Ford Coppola", "Drammatico"))
my_catalog.add_movie(Movie("Pulp Fiction", "Quentin Tarantino", "Thriller"))
my_catalog.add_movie(Movie("Inception", "Christopher Nolan", "Sci-Fi"))
my_catalog.add_movie(Movie("Le Iene", "Quentin Tarantino", "Thriller"))

print("Film drammatici:", [str(movie) for movie in my_catalog.get_movies_by_genre("Drammatico")])
print("Film di Quentin Tarantino:", [str(movie) for movie in my_catalog.get_movies_by_director("Quentin Tarantino")])'''