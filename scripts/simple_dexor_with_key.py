encoded_password = "I]{I\x14V\x17{WAGQV\x17{TS@"
decoded_password = ''.join(chr(ord(c) ^ 0x24) for c in encoded_password)
print(f"Le mot de passe est : {decoded_password}")
