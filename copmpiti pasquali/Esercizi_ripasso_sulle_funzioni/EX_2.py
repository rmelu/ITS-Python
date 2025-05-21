from typing import Dict, Any, Optional

def trova_chiave_per_valore(dizionario: Dict[Any, Any], valore: Any) -> Optional[Any]:
    for chiave, val in dizionario.items():
        if val == valore:
            return chiave
    return None

# Esempio di utilizzo (come nei tuoi test):
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))