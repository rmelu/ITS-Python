'''file = open("example.txt", "a")

print(file)
file.close()'''
'''
with open("example.txt", "w") as file:

    stringa: str = "Ciao prima prova"
    file.write(stringa)
    pass

#reader contiene TextIowrapper'''


with open("example.txt", "r+") as file:  #altrimenti fai  w+
    print(file.read())