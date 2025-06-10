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
    def __init__(self, customer_id:str, nome:str, rented_movies:list[Movie]) -> None:
        self.customer_id = customer_id
        self.nome = nome
        self.rented_movies = rented_movies 

    def rent_movie(self, movie:Movie) -> bool:
        if movie in self.rent_movies:
            print(f"{self.movie_title}: è gia noleggiato.")

    def return_movie(self, movie:Movie) -> bool:
        if movie == self.rented_movie:
            print(f"{movie.title}: non è stato noleggiato da questo cliente.")                

class Video_Rental_Store:
    def __init__(self, movie:dict[str:Movie], customer:dict[str,Customer]) -> None:
        self.movie = movie
        self.customer = customer


    def add_movie(self, movie_id: str, title: str, director: str) -> bool:
        if self.movie_id == movie_id:
            print(f"Il film con ID {self.movie_id}: esiste gia.")


    def register_customer(self, customer_id:str, name:str) -> bool:
        if self.customer_id == customer_id:
            print(f"Il cliente con ID {customer_id}: è gia Registrato.")
        else:
            print(f"Il cliente con ID{customer_id}: non è Registrato.")


    def rent_movie(self, customer_id:str, movie_id:str) -> bool:
        if self.customer_id == self.videoRentalStrore:
            raise True
        else:
            print(f"{movie_id}: non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str) -> bool:
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if not customer or not movie:
            print("Cliente o film non trovato.")
            return False

        if movie in customer.rented_movies:
            customer.rented_movies.remove(movie)
            print(f"'{customer.name}' ha restituito '{movie.title}'.")
            return True
        else:
            print(f"Il film '{movie.title}' non risulta noleggiato da '{customer.name}'.")
            return False
        
    def return_movie(self, customer_id: str, movie_id: str) -> bool:
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)
        if not customer or not movie:
            print("Cliente o film non trovato.")
            return False
        if movie in customer.rented_movies:
            customer.rented_movies.remove(movie)
            print(f" {customer.nome} ha restituito {movie.title}.")
            return True
        else:
            print(f" {movie.title} non risulta noleggiato da {customer.nome}.")
            return False
    def get_rented_movies(self, customer_id:str ) -> list[Movie]:
        customer = self.customers.get(customer_id)
        if not customer:
            print(f"Cliente con ID {customer_id} non trovato.")
            return []
        return customer.rented_movies
    

if __name__ == "__main__":
    print("__Start Test__")
    movie = Movie("001", "ollala", "Gioia", False)
    customer = Customer ("001", "Gioia", [])
    Video_Rental_Store = Video_Rental_Store({"001": movie}, {"001": customer} )
    print("Test di creazione del film e del cliente:")
    print(f"Film: {movie.title}, Regista: {movie.director}, ID: {movie.movie_id} - Noleggio: {movie.is_rented}")
    

print("\n")
print("\n Fine")