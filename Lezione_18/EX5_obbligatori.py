class FormulaError(Exception):
    pass

def calculate(expression: str) -> float:
    parts:list[str] = expression.split()
    if len(parts) != 3:
        raise FormulaError("Formato non valido. Usa: numero operatore numero")
    try:
        a:float = float(parts[0])
        op:str = parts[1]
        b:float = float(parts[2])
    except ValueError:
        raise FormulaError("I numeri non sono validi.")
    if op not in ('+', '-'):
        raise FormulaError("Operatore non valido. Solo + o - ammessi.")
    return a + b if op == '+' else a - b

# Esempio
print(calculate("3 + 5"))