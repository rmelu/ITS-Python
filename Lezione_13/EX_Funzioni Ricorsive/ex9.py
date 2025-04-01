def vowelRemover(stringa):
    vocali = "aeiouAEIOU"
    if not stringa:     #caso base stringa vuota
        return ""
    if stringa[0] in vocali:
        return vowelRemover(stringa[1:])#rimuovi la vocale     
    else:
        return stringa[0] + vowelRemover (stringa[1:])   #mantieni la consonante
    
print(vowelRemover("ciao, come, stai?"))  # OP:  C, cm st?
print(vowelRemover("AEIOU"))   # OP: ""(nn stampa nulla)
print(vowelRemover("Python"))  # OP:   pythn

'''
#  [1:] --> vuol dire estrare una sotto sequenza a partire dall'indice 1 (incluso) fino alla fine della sequenza 
#ESEMPIO
stringa = "Python"
sottostringa = stringa [1:] #sottostringa conterrà "ython"

lista = [10, 20, 30, 40, 50]
sottostringa = lista[1:]  # sottostringa conterrà [20, 30, 40, 50]


# [:1] --> in questo caso etrae una sottosequenza dall'inizio della sequenza fino all'indice 1 escluso
#ESEMPIO
stringa = "Python"
sottostringa = stringa [:1] #sottostringa conterrà "P"

lista = [10, 20, 30 ,40 ,50]
sottostringa = lista [:1]  #sottostringa conterrà [10]

questo metodo si usa nelle stringhe e nelle liste
    '''