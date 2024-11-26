# Données d'entrée
s1 = "1010101010101010101010101010101010"  # Chaîne binaire
s2 = 0x44585d6b2368737c65252166234f20626d  # Hexadécimal, déjà interprété comme entier

# Conversion de `s1` en entier
s1_int = int(s1, 2)

# Effectuer le XOR
result = s2 ^ s1_int

# Affichage des résultats dans différents formats
print(f"Résultat en binaire : {bin(result)}")
print(f"Résultat en hexadécimal : {hex(result)}")

