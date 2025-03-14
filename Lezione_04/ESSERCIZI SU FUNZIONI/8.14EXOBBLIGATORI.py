'''def make_car(produttore, modello, **info_aggiuntive):
    auto = {
        'produttore': produttore,
        'modello': modello,
    }
    auto.uopdate(info_aggiuntive)     #aggiungi informazioni extra
    return auto
auto_mia = make_car('subaru', 'outback', colore='blu', pacchetto_traino=True)
print(auto_mia)'''


#altrimenti
def make_car(produttore, modello, **info_aggiuntive):
    auto = {
        'produttore': produttore,
        'modello': modello,
    }
    for chiave, valore in info_aggiuntive.items():
        auto[chiave] = valore
    return auto
auto_mia = make_car('yaris', 'toyota', colore='blu', pacchetto_traino=True)
print(auto_mia)