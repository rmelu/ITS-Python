#EX-3.5
name:list = ["Federico:","Flavio","Leonardo"]
mess:list = ["caro amico ti invitiamo a mangiare sushi <3","ti invitiamo per una bevuta","sei stato invitato per un caffe."]
name[0] = "Marco" 
name.extend(["Marco", "Claudia"])
mess.extend(["sei invitato per un apperitivo dell'ultimo momento", "ti invito per un tè."]) 
#mess.extend("Claudia ti mando un invito dell'ultimo minuto")
for i in range (len(name)):
    print(name[i],mess[i])
print("purtroppo federico non può esserci :-(")
print("cari amici attendiamo un v.s riscontro grazie <3")