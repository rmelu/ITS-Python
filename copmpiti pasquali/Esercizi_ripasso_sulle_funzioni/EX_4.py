from typing import List, Dict

def aggrega_voti(voti: List[Dict[str, int]]) -> Dict[str, List[int]]:
    risultato: Dict[str, List[int]] = {}
    for record in voti:
        nome = record['nome']
        voto = record['voto']
        if nome in risultato:
            risultato[nome].append(voto)
        else:
            risultato[nome] = [voto]
    return risultato

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

print(aggrega_voti([]))