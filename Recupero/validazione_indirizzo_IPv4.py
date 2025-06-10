def is_valid_ipv4(adress: str) -> bool:
    """
    Verifica se un indirizzo IP è valido secondo lo standard IPv4.
    
    :param adress: str - Indirizzo IP da verificare
    :return: bool - True se l'indirizzo IP è valido, False altrimenti
    """
    parts = adress.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
        if len(part) > 1 and part[0] == '0':  # Evita numeri con zeri iniziali
            return False
    
    return True

print(is_valid_ipv4("192.168.0.1")) # True, indirizzo IP valido
print(is_valid_ipv4("255.255.255.255")) # True, indirizzo IP valido
print(is_valid_ipv4("256.100.10.1"))  # False, 256 non è valido
print(is_valid_ipv4("192.168.1"))  # False, manca un ottetto
print(is_valid_ipv4("192.168.1.a"))  # False, contiene caratteri non numerici