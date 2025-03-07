città = {
    "Parigi": {
        "Paese" : "Francia",
        "Popolazione" : 2141000,
        "Fatto" : "La Torre Eiffel, uno dei simboli iconici di Parigi e della Francia, è una strutura in ferro battuto a traliccio, alta 330 metri (antenna inclusa). Costruita per l'Esposizione Universale del 1889, inizialmente doveva essere una struttura temporanea, ma la sua  importanza come antenna di telecomunicazioni la salvò della demolizione.",
        "Clima" : "Temperato oceanico",
        "Lingua" : "Francese"
    }
}
#stampa delle informazioni su ogni città
for nome_città in città:
    print("Informazioni si", nome_città + ":")
    print("Paese:", città[nome_città]["Paese"])
    print("Popolazione:", città[nome_città]["Popolazione"])
    print("Fatto:", città[nome_città]["Fatto"])
    print("Clima:", città[nome_città]["Clima"])
    print("Lingua:", città[nome_città]["Lingua"])
    print()  #lasciare una rigua vuora