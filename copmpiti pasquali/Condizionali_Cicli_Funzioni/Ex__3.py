def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
        return stipendio
    elif ore_lavorate > 40:
        ore_straordinario = ore_lavorate - 40
        stipendio_base = 40 * 10
        paga_straordinario = ore_straordinario * 15
        stipendio_totale = stipendio_base + paga_straordinario
        return stipendio_totale
    
print(calcola_stipendio(40))