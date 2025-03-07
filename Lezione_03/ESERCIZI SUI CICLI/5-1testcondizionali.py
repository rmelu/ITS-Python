# Test condizionali
car = 'subaru'
#test 1: L'auto è una 'subaru??
print("Is car == 'subaru'? I ptredict True. ")
print(car == 'subaru')  #Risultato: True

#Test 2: L'auto è un 'audi'?
print("\nIs car == 'Audi'? I predict False. ")
print(car == 'Audi')  #Risultato: False

#Test 3: L'auto è diversa da 'BMW'
print("\nIs car != 'BMW'? I pedict True.")
print(car != 'BMW')   #Risultato: True

#Test 4: L'auto è diversa da 'subaru'
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')   #Risultato: False

#Test 5: L'auto è 'subaru' (case insensitive)?
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU') #Risultato: True

#Test 6: L'auto è 'subaru' (case sensitive)?
print("\nIs car.lower() == 'SUBARU'? I pedict False.")
print(car.lower() == 'SUBARU') #Risultato: False

#Test 7: La lunghezza dell'auto è 6?
print("\n Is len(car) == 6? I predict True. ")
print(len(car) == 6)   #Risultato: True

#Test 8: La lunghezza del nome dell'auto è 5?
print("\nIs len(car) == 5? I predict False.")
print(len(car) == 5 )  #Risultato: False

#test 9: 's' è presente nel nome dell'auto?
print("\nIs 's' in car? I predict True.")
print('s' in car) #Risultato: True

#Test 10: 'a' è presente nel nome dell'auto?
print("\nIs 'a' not in car? I predict False.")
print('a' not in car)  #Risultato: False