import zipfile
import os
import base64
import zlib

# Paramètres
input_png = "input.png"  # Votre fichier PNG existant
input_zip = "suspicious.zip"  # Le fichier ZIP existant, déjà protégé par mot de passe
output_polyglot = "polyGoat.png"  # Le fichier polyglotte final
fake_flag = "FW_{C0nt1nu35_d3_ch3rch3r_ch3r5_4m1}"  # Faux flag dans le PDF
real_flag = "FW_{70u7_c3_73mp5_p0ur_uN_s1mpl3_p0l1gl0773}"  # Vrai flag dans le ZIP

# Étape 1 : Charger le PNG existant
with open(input_png, "rb") as f:
    png_data = f.read()

# Étape 2 : Créer un contenu PDF avec texte invisible
# Encode le faux flag en base64 pour le rendre moins évident
encoded_fake_flag = "46 57 5f 7b 43 30 6e 74 31 6e 75 33 35 5f 64 33 5f 63 68 33 72 63 68 33 72 5f 63 68 33 72 35 5f 34 6d 31 7d"

# Texte PDF avec flag encodé et ajout de quelques caractères invisibles
pdf_content = (
    f"q\n"
    f"1 1 1 rg\n"  # Couleur blanche (invisible sur fond blanc)
    f"BT /F1 12 Tf 50 700 Td ({encoded_fake_flag}) Tj ET\n"  # Faux flag encodé
    f"Q\n"
).encode()

pdf_header = (
    b"%PDF-1.4\n"
    b"1 0 obj\n"
    b"<< /Type /Catalog /Pages 2 0 R >>\n"
    b"endobj\n"
    b"2 0 obj\n"
    b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n"
    b"endobj\n"
    b"3 0 obj\n"
    b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> >> >>\n"
    b"endobj\n"
    b"4 0 obj\n"
    b"<< /Length " + str(len(pdf_content)).encode() + b" >>\n"
    b"stream\n" + pdf_content + b"\nendstream\n"
    b"endobj\n"
)
xref_start = len(pdf_header)
pdf_footer = (
    b"xref\n"
    b"0 5\n"
    b"0000000000 65535 f \n"
    b"0000000010 00000 n \n"
    b"0000000067 00000 n \n"
    b"0000000128 00000 n \n"
    b"0000000194 00000 n \n"
    b"trailer\n"
    b"<< /Root 1 0 R /Size 5 >>\n"
    b"startxref\n"
    + str(xref_start).encode() + b"\n"
    b"%%EOF"
)
pdf_data = pdf_header + pdf_footer

# Étape 3 : Lire le fichier ZIP existant
with open(input_zip, "rb") as zip_file:
    zip_data = zip_file.read()

# Étape 4 : Obfuscation des métadonnées
metadata = zlib.compress(b"Tu ne trouveras rien ici, espece de paresseux(se).\n" * 10)

# Étape 5 : Combinaison finale pour créer le polyglot
with open(output_polyglot, "wb") as polyglot_file:
    polyglot_file.write(png_data)         # Ajouter le PNG
    polyglot_file.write(metadata)         # Ajouter les métadonnées compressées
    polyglot_file.write(pdf_data)         # Ajouter le faux flag dans le PDF
    polyglot_file.write(metadata)         # Ajouter des métadonnées supplémentaires
    polyglot_file.write(zip_data)         # Ajouter le fichier ZIP protégé par mot de passe

print(f"Fichier polyglotte sécurisé créé : {output_polyglot}")
