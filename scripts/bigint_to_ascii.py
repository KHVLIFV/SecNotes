# Big integer
big_int = 31381767556396068451396213107418146737161460075387838039325522269201190105981

# Étape 1 : Convertir en bytes (hexadécimal d'abord, puis en bytes)
hex_representation = hex(big_int)[2:]  # Supprime le préfixe "0x"

# Assurez-vous que la longueur est paire (pour convertir en bytes)
if len(hex_representation) % 2 != 0:
    hex_representation = "0" + hex_representation

# Convertir l'hexadécimal en bytes
byte_data = bytes.fromhex(hex_representation)

# Étape 2 : Décoder en ASCII (si c'est interprétable en ASCII)
try:
    ascii_string = byte_data.decode('ascii')
    print(f"Chaîne ASCII : {ascii_string}")
except UnicodeDecodeError:
    print("Les données ne sont pas interprétables en ASCII.")
