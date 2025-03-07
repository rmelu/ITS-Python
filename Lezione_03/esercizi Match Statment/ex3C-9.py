x = int(input("Inserisci la cordinata x: "))
y = int(input("Inserisci la cordinata y: "))

punto = (x, y)

match punto:
    case(0, 0):
        print("Il punto si trova nell'origine.")
    case (_, 0):
        print("Il punto si trova sull'asse X. ")
    case(0, _):
        print("Il punto si trova sull'asse Y. ")
    case(x, y) if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante. ")
    case(x, y) if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante. ")
    case(x, y) if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante. ")
    case(x, y) if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante. ")
    case _:
        print( )