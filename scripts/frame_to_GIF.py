from PIL import Image

# Chargez les frames découpées
frames = [Image.open(f"frame_{i}.png") for i in range(9)]

# Créez le GIF
frames[0].save("output.gif", save_all=True, append_images=frames[1:], duration=100, loop=0)
