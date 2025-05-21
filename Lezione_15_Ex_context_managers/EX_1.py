
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None # Inizializza l'attributo file a None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"File '{self.filename}' aperto in modalità '{self.mode}'.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"File '{self.filename}' chiuso.")
        if exc_type:
            print(f"Si è verificata un'eccezione: {exc_val}")
            # Se ritorni True, l'eccezione viene soppressa.
            # Qui la lasciamo propagare, quindi non ritorniamo nulla (o None).
            return False


print("---esempio1: scrittura ---")
with FileManager('example.txt', 'w') as f:
    f.write('Hello world\n')
    f.write('this is a  test line.\n')
print("scrittura completata.\n")


#verifica il contenuto del file (riaprendo in lettura)
print("--- verifico il contenuto---")
with FileManager('example.txt', 'r') as f:
    content = f.read()
    print("contenuto di example.txt:")
    print(content)
print("lettura completata.\n")


#esempio2: simulazione di un errore all'interno del blocco 'with'
print("---esempio 2: Errore simulato---")
try:
    with FileManager('another_example.txt', 'w') as f:
        f.write('Prima riga.\n')
        #provo a fare un'operazione non valida per generare un errore
        #ad esmpio, dividere per zero
        result = 10 / 0
        f.write('questa riga non verrà scritta.\n')
except ZeroDivisionError:
    print("cattura l'eccezione ZeroDivisionErrore all'esterno del context manager.")
print("Gestione errore completata.\n")

# Nota: nonostante l'errore, il file 'another_example.txt' saraà comunque chiuso da __exit__.
# Puoi verificarlo aprendolo manualmente o tentando di accedere.
    
