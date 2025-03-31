def inserisci_temperatura(giorno):
    while True:
        try:
            temp = float(input(f"inserisci la temperatura del giorno{giorno}"))
            if temp < -100 or temp > 100: #intervallo di temperatura accettabile
                print("per favore, inserisci una temperatura valida.")
            else:
                return temp
        except ValueError:
            print("input non valido. per favore, inserisci un numero.")
def calcola_media(temperature):
    return sum(temperature) / len(temperature)

def verifica_temperature(temperature):
            if all("10 <= temp <=30 for temp in temperature"):
                print("temperatura ok")
def trova_giorni_estremi(temperature):
    giorno_max = temperature.index(max(temperature)) + 1
    giorno_min = temperature.index(min(temperature)) + 1
    print(f"la temperatura piu alta è stata regostrata il giorno {giorno_max}")






firmware/ e un softwere
è un softwere che non viene manipolato da utenti
firmwere viene utilizzato per avviare il caricamento del avviamento
non volatile memoria: ce la rom che (ride only memori )
eprom erasable programmabile read-only memory.
eeprom: eletrically erasable programmable ready_only memory.
falsh memory : sono memorie di massa tipo ids ecc....

 motherboard/2
la schieda madre: si trova su tutti tipi di dispositivi. nel contesto del computer troviamo
gli slot per la memoria ram, 
bios/uefi per avviare la macchina 

basic input/output system(bios)
serve per avviare il sistema operativo,
all'interno abbiamo bios
il bios per il ricaricamento usa bootstrap/1.

uefi(unifiend extensibile firmware interfece) 
sarebbe il firmweare utilizzato da ....

anche i driver sono dei (soft ware) ,
differenze tra frim were e driver
frimwere:  
driver: 
la funzione e la posizione gli distingue molto.

sistema operazione : gestisce tra lutenti e la hardweare

*classification based on processing features:  mono task opereting.
*multi task operating sistems
*multi threading operating system
