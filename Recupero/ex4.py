def check_conditions(X, Y, Z):
    '''i = 5
    while i <= 45:
        print(i)
        i += 10'''
    if X and (Y or Z):
        return "Azione permessa"
    else:
        return "Azione negata"
    
print(check_conditions(True, True, False))
print(check_conditions(True, False, False))