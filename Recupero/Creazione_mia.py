'''from turtle import *

speed(-100)
bgcolor("black")
color("#0be0fc")
for i in range(170):
    forward(i)
    right(240)
    for j in range(3):
        forward(i)
        left(30)
        circle(40, 30)
    hideturtle()

done()'''










from turtle import *

speed(-100)
bgcolor("black")
color("#0be0fc")

# Parte del codice originale per il disegno
for i in range(170):
    forward(i)
    right(240)
    for j in range(3):
        forward(i)
        left(30)
        circle(40, 30)

hideturtle() # Nasconde la tartaruga dopo aver completato il disegno

# --- Codice per scrivere una singola lettera ---

# Solleva la penna per spostare la tartaruga senza disegnare
penup()

# Sposta la tartaruga alla posizione desiderata per la lettera
# Puoi modificare queste coordinate (x, y) per posizionare la lettera
goto(0, -100) # Esempio: X=0 (centro orizzontale), Y=-100 (un po' in basso)

# Abbassa la penna per iniziare a scrivere
pendown()

# Scrivi la lettera desiderata
# CAMBIA "A" CON LA LETTERA CHE VUOI VISUALIZZARE
# Puoi anche modificare il font, la dimensione e lo stile
write("A", font=("Verdana", 48, "bold")) # Esempio: font "Verdana", dimensione 48, stile "bold"

# Questo comando mantiene la finestra aperta finché non viene chiusa manualmente
done()


