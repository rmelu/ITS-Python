class Book:
    """
    Rappresenta un libro con titolo, autore e ISBN.
    """
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # Aggiunto per tracciare lo stato di prestito

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa leggibile del libro.
        """
        status = " (Prestato)" if self.is_borrowed else ""
        return f'"{self.title}" di {self.author} (ISBN: {self.isbn}){status}'

    @classmethod
    def from_string(cls, book_str: str):
        """
        Metodo di classe per creare un'istanza di Book da una stringa.
        Formato stringa: "Titolo, Autore, ISBN"
        """
        parts = [part.strip() for part in book_str.split(',')]
        if len(parts) != 3:
            raise ValueError("Formato stringa del libro non valido. Atteso: 'Titolo, Autore, ISBN'")
        return cls(parts[0], parts[1], parts[2])

class Member:
    """
    Rappresenta un membro della biblioteca con nome e ID membro.
    Tiene traccia dei libri presi in prestito.
    """
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # Lista di oggetti Book

    def borrow_book(self, book):
        """
        Aggiunge un libro alla lista dei libri presi in prestito dal membro.
        """
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"'{book.title}' aggiunto ai libri presi in prestito da {self.name}.")
        else:
            print(f"'{book.title}' è già nella lista dei libri presi in prestito da {self.name}.")

    def return_book(self, book):
        """
        Rimuove un libro dalla lista dei libri presi in prestito dal membro.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"'{book.title}' restituito da {self.name}.")
            return True
        else:
            print(f"Errore: '{book.title}' non è tra i libri presi in prestito da {self.name}.")
            return False

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa leggibile del membro.
        """
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Membro: {self.name} (ID: {self.member_id}) - Libri presi: {', '.join(borrowed_titles) if borrowed_titles else 'Nessuno'}"

    @classmethod
    def from_string(cls, member_str: str):
        """
        Metodo di classe per creare un'istanza di Member da una stringa.
        Formato stringa: "Nome, Member-ID"
        """
        parts = [part.strip() for part in member_str.split(',')]
        if len(parts) != 2:
            raise ValueError("Formato stringa del membro non valido. Atteso: 'Nome, Member-ID'")
        return cls(parts[0], parts[1])

class Library:
    """
    Gestisce la collezione di libri e membri.
    """
    total_books = 0  # Attributo di classe per tenere traccia del numero totale di libri

    def __init__(self, name: str = "Biblioteca Comunale"):
        self.name = name
        self.books = []  # Lista di oggetti Book
        self.members = []  # Lista di oggetti Member

    def add_book(self, book: Book):
        """
        Aggiunge un libro alla libreria e incrementa il conteggio totale dei libri.
        """
        if not isinstance(book, Book):
            raise TypeError("L'oggetto da aggiungere deve essere un'istanza di Book.")
        if book not in self.books:
            self.books.append(book)
            Library.total_books += 1
            print(f"Aggiunto alla libreria: {book.title}")
        else:
            print(f"Il libro '{book.title}' è già presente nella libreria.")

    def remove_book(self, book: Book):
        """
        Rimuove un libro dalla libreria e decrementa il conteggio totale dei libri.
        """
        if book in self.books:
            if book.is_borrowed:
                print(f"Impossibile rimuovere '{book.title}': il libro è attualmente in prestito.")
                return False
            self.books.remove(book)
            Library.total_books -= 1
            print(f"Rimosso dalla libreria: {book.title}")
            return True
        else:
            print(f"Errore: '{book.title}' non trovato nella libreria.")
            return False

    def register_member(self, member: Member):
        """
        Registra un nuovo membro nella biblioteca.
        """
        if not isinstance(member, Member):
            raise TypeError("L'oggetto da registrare deve essere un'istanza di Member.")
        if member not in self.members:
            self.members.append(member)
            print(f"Membro registrato: {member.name}")
        else:
            print(f"Il membro '{member.name}' è già registrato.")

    def lend_book(self, book: Book, member: Member):
        """
        Presta un libro a un membro, controllando disponibilità e registrazione.
        """
        if not isinstance(book, Book) or not isinstance(member, Member):
            print("Errore: Entrambi gli argomenti devono essere istanze di Book e Member.")
            return False

        if member not in self.members:
            print(f"Errore: Il membro '{member.name}' non è registrato in questa libreria.")
            return False

        if book not in self.books:
            print(f"Errore: Il libro '{book.title}' non è disponibile in questa libreria.")
            return False

        if book.is_borrowed:
            print(f"Errore: Il libro '{book.title}' è già in prestito.")
            return False
        
        # Effettua il prestito
        book.is_borrowed = True
        member.borrow_book(book)
        print(f"Prestito effettuato: '{book.title}' a {member.name}.")
        return True

    def receive_returned_book(self, book: Book, member: Member):
        """
        Gestisce la restituzione di un libro da parte di un membro.
        """
        if not isinstance(book, Book) or not isinstance(member, Member):
            print("Errore: Entrambi gli argomenti devono essere istanze di Book e Member.")
            return False

        if book in self.books and book.is_borrowed:
            if member.return_book(book): # Tenta di rimuovere dalla lista del membro
                book.is_borrowed = False
                print(f"'{book.title}' è stato restituito e ora è disponibile.")
                return True
            else:
                print(f"Errore nella restituzione: '{book.title}' non era in prestito a {member.name}.")
                return False
        else:
            print(f"Errore: '{book.title}' non è in prestito o non appartiene a questa libreria.")
            return False

    def __str__(self):
        """
        Restituisce una rappresentazione in stringa della biblioteca con libri e membri.
        """
        book_list = "\n  ".join([str(book) for book in self.books]) if self.books else "  Nessun libro."
        member_list = "\n  ".join([str(member) for member in self.members]) if self.members else "  Nessun membro."
        return (f"--- {self.name} ---\n"
                f"Libri disponibili ({len(self.books)}):\n  {book_list}\n"
                f"Membri registrati ({len(self.members)}):\n  {member_list}")

    @classmethod
    def library_statistics(cls):
        """
        Metodo di classe per stampare il numero totale di libri gestiti da tutte le istanze della libreria.
        """
        print(f"\nStatistiche Biblioteca: Numero totale di libri creati: {cls.total_books}")

if __name__ == "__main__":
    print("### Inizializzazione della Biblioteca ###")
    my_library = Library("La Nostra Biblioteca")
    print(my_library)
    Library.library_statistics()

    print("\n### Creazione di Libri (usando from_string) ###")
    book1 = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
    book2 = Book.from_string("Il Signore degli Anelli, J.R.R. Tolkien, 123456789")
    book3 = Book.from_string("1984, G. Orwell, 000111222")
    book4 = Book("Fiori per Algernon", "Daniel Keyes", "333444555") # Creazione "normale"

    print("\n### Creazione di Membri (usando from_string) ###")
    member1 = Member.from_string("Mario Rossi, M001")
    member2 = Member.from_string("Laura Bianchi, M002")
    member3 = Member("Giuseppe Verdi", "M003") # Creazione "normale"

    print("\n### Aggiunta di libri e registrazione membri alla biblioteca ###")
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4)

    my_library.register_member(member1)
    my_library.register_member(member2)
    my_library.register_member(member3)

    print("\n### Stato della biblioteca PRIMA di prestare libri ###")
    print(my_library)
    Library.library_statistics()

    print("\n### Simulazione Prestiti ###")
    my_library.lend_book(book1, member1) # Mario prende "La Divina Commedia"
    my_library.lend_book(book3, member2) # Laura prende "1984"
    my_library.lend_book(book2, member1) # Mario prende "Il Signore degli Anelli"

    # Tentativo di prestare un libro già in prestito
    my_library.lend_book(book1, member2)

    # Tentativo di prestare un libro non esistente o a un membro non registrato
    book_fake = Book("Libro Falso", "Autore Falso", "000000000")
    my_library.lend_book(book_fake, member1)
    member_fake = Member("Membro Falso", "M999")
    my_library.lend_book(book1, member_fake)

    print("\n### Stato della biblioteca DOPO aver prestato libri ###")
    print(my_library)
    print(member1) # Stampa lo stato dei libri presi dal membro
    print(member2)
    Library.library_statistics()

    print("\n### Simulazione Restituzioni ###")
    my_library.receive_returned_book(book1, member1) # Mario restituisce "La Divina Commedia"
    my_library.receive_returned_book(book2, member1) # Mario restituisce "Il Signore degli Anelli"

    # Tentativo di restituire un libro non in prestito o da un membro sbagliato
    my_library.receive_returned_book(book3, member1) # Laura ha "1984", non Mario
    my_library.receive_returned_book(book4, member2) # book4 non è in prestito

    print("\n### Stato della biblioteca DOPO le restituzioni ###")
    print(my_library)
    print(member1)
    print(member2)
    Library.library_statistics()

    print("\n### Rimozione di un libro dalla biblioteca ###")
    my_library.remove_book(book4) # Rimuovi un libro non in prestito
    my_library.remove_book(book3) # Tentativo di rimuovere un libro ancora in prestito

    print("\n### Stato finale della biblioteca ###")
    print(my_library)
    Library.library_statistics()