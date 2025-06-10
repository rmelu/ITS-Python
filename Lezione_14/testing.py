'''assert 1 > 0 #qui non succede nulla va tutto bene
assert 1 < 0  #da errore, è un tipo di errore viene elevato quando la condizione è falsa
'''
n = 0
assert 1 < n, 'The condition is False'

#assert <condition being tested>, <error message to be display>
