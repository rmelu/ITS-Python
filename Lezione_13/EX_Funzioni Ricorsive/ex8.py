def vowelsCounters(s : str)-> str:
    if not s:
        return 0
    else:
        prima_lettera = s[0].lower()
        if prima_lettera  in 'aeiou':    #aeiou serve per determinare se una letter è vocale o meno!!!!!
            return 1 + vowelsCounters(s[1:])
        else:
            return vowelsCounters(s[1:])
print(vowelsCounters("ciao, come  andiamo oggi ?"))  #caio = c [non vocale], i = [vocale] a = [vocale], o = [vocale]
print(vowelsCounters("secondo tenttativo"))
print(vowelsCounters("nn c! m3tt@ v@c@l!"))  #stamopa zero perche ho scrito evitando di mettere aeiou :-) top!