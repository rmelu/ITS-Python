'''def build_profile(nome, cognome, **info_utente):
    profilo = (f"{nome} {cognome}")
    for chiave, valore in info_utente.items():
        profilo += (f", {chiave} {valore}")
    return profilo
profilo_utente = build_profile("mario", "rossi", eta=30, citta="roma", professione="programmatore")
print(profilo_utente)'''



#altrimenti
def build_profile(info_utente):
    for utente in info_utente:
        print(utente)
profilo = [
    "nome:" "mario",
    "cognome:" "rossi",
    "età:" '67',
    "professione:" "programmatore"
    ]
build_profile(profilo)
print()


