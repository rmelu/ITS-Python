ipotenusa = 5
cateto_b = 3     #CHIAMIAMO CATETO_b PER CHIAREZZA
if ipotenusa**2 > cateto_b**2:
    cateto_c = (ipotenusa**2 - cateto_b**2)**0.5   #CALCOLIAMO CATETO C
    print("La misura del cateto 'c' è: cateto_c ") 
else:
    print("Error: l'ipotenusa ")