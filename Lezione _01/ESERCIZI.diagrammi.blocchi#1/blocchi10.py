#distribuzione burza di studio
reddito = int(input("Inserisci reddito: "))
media = int(input("inserisci la media dei voti: "))
if reddito < 20000 and media >= 27:
    print("Borza di studio approvata :-) ")
#if reddito > 20000 and media > 27:
 #   print("Borza di studio approvata, sia per il voto alto che per il reddito, complimenti campione :)")
elif reddito >= 20000 and media >= 27:
    print("Borza di studio rifiutata, reddito molto alto")
elif reddito < 20000 and media < 27:
    print("Borza di studio rifiutata, media voto insufficiente :-( )")
else:
    print("Borza di studio rifiutata, reddito e media voti insufficiente ")