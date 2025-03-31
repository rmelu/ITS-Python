giorno = int(input("Iserisci giorno: "))
mese = int(input("Inserisci il mese: "))
data = (giorno, mese)
#import datetime -->       il modulo imoprt datetime è un modulo standard di python che fornisce classi per lavorare  con date e orari!!!
#primo_giorno_mese = oggi.replace(day = 1)  -->     replace serve per sostituire una vecchia stringa con una nuova!!!
#for mese in range(1, 13): -->              in questo caso non serve ma se lo includo ripete tredici volte ciò che da in output!!!

#serve per creare anno.mese.giorno odierna
#import datetime             -->            in questo caso ottengo il singolo anno,mese,giorno  
#oggi = datetime.date.today()
#print()
match data:
        case (1, 1):
            print("capodanno *.*^*.*^*.*^*.*^*")
        case (14, 2):
            print("San valentino <3 :-* ")
        case (2, 5):
            print("Festa della Repubblica Italiana <-X->. ")
        case (15, 8):
            print("Ferragosto ~~~~zzz~~~ ")
        case (31, 10):
            print("Halloween °;° °;° °;° ")
        case (25, 12):
            print("Buon Natale :-) :) ")
        case (17, 11):
          print("HAPPY BIRTHDAY HONEY SWEET GIRL <3 ")
        case _: #case senza valore altrimenti, IL "TRATTINO _" chiamato anche WILDCARD (CHE CONRRISPONDE A QUALSIASI VALORE).
            print("Non ci sono festivita ti tocca lavorare :-O :(  ")


















                                                                                                                                            