#Definisco le approssimazione di pi da raggingere
pi_3_14 = 3.14
Pi_3_141 = 3.141
pi_3_1415 = 3.1415
pi_3_14159 = 3.14159
#Calcola i termini per pi ~ 3.14
pi = 0
n = 1
termini_3_14 = 0
segno = 1

while abs(pi - pi_3_14) > 1e-6:
    pi += segno * 4 / (2 * n -1)
    n += 1
    termini_3_14 += 1
    print(f"Termini necessari per pi = 3.14: {termini_3_14}")

#Calcolo i termini per pi ~ 3.141
pi = 0  #Reset di pi 
n = 1   #Reset di n
termini_3_141 = 0
segno = 1 #Reset del segno
while abs(pi - Pi_3_141) > 1e-6:
    pi += segno * 4 / (2 *n -1)
    segno *= -1
    n += 1
    termini_3_141 += 1
print(f"Termini necessari per pi = 3.141: {termini_3_141}")

#Calcolo i termini per pi ~ 3.1415
pi = 0   #Reset di pi
n = 1    # Reset di n
termini_3_1415 = 0
segno = 1     #Reset del segno
while abs(pi - pi_3_1415) > 1e-6:
    pi += segno * 4 / (2 * n - 1)
    segno *= -1
    n += 1
    termini_3_1415 += 1
print(f"Termini necessari per pi = 3.1415: {termini_3_1415}")

#Calcolo i termini per pi ~ 3.14159
pi = 0     #Reset di pi
n = 0     #Reset di n
termini_3_14159 = 0
segno = 1   #Reset del segno
while abs(pi - pi_3_14159) > 1e-6:
    pi += segno
    segno *= -1 
    n += 1
    termini_3_14159 += 1
print(f"Termini necessari per pi = 3.14159: {termini_3_14159}")




