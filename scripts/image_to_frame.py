from PIL import Image

# Chargez l'image
img = Image.open("original_image.png")

# Dimensions de l'image
width, height = img.size

# Découpage en 3 lignes et 3 colonnes
frame_width = width // 3
frame_height = height // 3

# Créez les frames
frames = []
for i in range(3):  # 3 lignes
    for j in range(3):  # 3 colonnes
        left = j * frame_width
        top = i * frame_height
        right = left + frame_width
        bottom = top + frame_height
        frames.append(img.crop((left, top, right, bottom)))

# Sauvegardez les frames
for idx, frame in enumerate(frames):
    frame.save(f"frame_{idx}.png")
