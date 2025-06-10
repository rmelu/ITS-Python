class Movie:
    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    
    def rent(self) -> bool:
        if self.is_rented:
            print(f"{self.title}: è gia noleggiato.")
        else:
            print(f"{self.title}: non è ancora noleggiato")
    
    def return_movie(self) -> bool:
        if self.is_rented == False:
            print(f"{self.title}: è gia noleggiato.")
        else:
            print(f"{self.title}: non è stato noleggiato dal cliente.")

class Customer:
    def __init__(self, customer_id:str, nome:str) -> None:
        self.customer_id: str = customer_id
        self.nome: str = nome
        self.rented_movies: list[Movie] = [] 

    def rent_movie(self, movie:Movie) -> None:
        if movie.is_rented:
            print(" è gia noleggiato.")
        else:
            movie.rent()
            self.rented_movies.append(movie)
            

    def return_movie(self, movie:Movie) -> None:
        if movie not in self.rented_movies:
            print("l'utente non ha il film noleggiato.")            
        else:
            self.rented_movies.remove(movie)

class Video_Rental_Store:
    def __init__(self, customer:dict[str,Customer] = None, movie:dict[str,Movie] = None):

        self.customers: dict[str, Customer] = customer if customer is not None else {}
        self.movies: dict[str, Movie] = movie if movie is not None else {}


    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        if movie_id not in self.movies:
            print("Il film è gia presente nel catalogo.")
        else:
            new_movie = Movie(movie_id, title, director,)
            self.movies[movie_id] = new_movie

    def register_customer(self, customer_id:str, name:str) -> None:
        if customer_id in self.customers:
            print(f"Il cliente con ID è gia Registrato.")
        else:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
            print(f"Il cliente con ID non è Registrato.")


    def rent_movie(self, customer_id:str, movie_id:str) -> None:

        if customer_id not in self.customers or movie_id not in self.movies:
            print("Cliente o film non trovato.")

        else:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)

    
    def return_movie(self, customer_id: str, movie_id: str) -> None:
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if customer_id not in self.customers or movie_id not in self.movies or movie not in customer.rented_movies:
            print("Cliente o film non trovato o il film non è stato noleggiato dal cliente.")
        else:
            customer: Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)


    def get_rented_movies(self, customer_id:str ) -> list[Movie]:
        if customer_id not in self.customers:
            print("Cliente non trovato.")
            return []
        else:
            customer = self.customers[customer_id]
            return customer.rented_movies
        

if __name__ == "__main__":
    Blockbuster: Video_Rental_Store = Video_Rental_Store()
    Blockbuster.add_movie("001", "Inception", "Christopher Nolan")
    Blockbuster.add_movie("002", "The Matrix", "Lana Wachowski, Lilly Wachowski")
    Blockbuster.register_customer("C001", "Alice")
    Blockbuster.register_customer("C002", "Bob")
    Blockbuster.rent_movie("C001", "001")
    Blockbuster.rent_movie("C002", "002")
    Blockbuster.return_movie("C001", "001")
    rented_movies = Blockbuster.get_rented_movies("C001")
    for movie in rented_movies:
        print(f"{movie.title} is rented by {movie.director}.")
    rented_movies = Blockbuster.get_rented_movies("C002")
    for movie in rented_movies:         
        print(f"{movie.title} is rented by {movie.director}.")
    Blockbuster.return_movie("C002", "002")
    rented_movies = Blockbuster.get_rented_movies("C002")
    for movie in rented_movies:
        print(f"{movie.title} is rented by {movie.director}.")
    Blockbuster.rent_movie("C001", "002")  # Attempt to rent a movie that is not available