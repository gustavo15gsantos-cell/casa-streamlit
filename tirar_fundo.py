from PIL import Image

# Abre a imagem original
img = Image.open("Tech-HOME.jpeg").convert("RGBA")
dados = img.getdata()

nova_imagem = []
# A cor do fundo da sua logo é um azul bem escuro (próximo de R:5, G:12, B:28)
for r, g, b, a in dados:
    # Se o pixel for muito escuro (faz parte do fundo), deixa 100% transparente
    if r < 25 and g < 35 and b < 55:
        nova_imagem.append((0, 0, 0, 0))
    else:
        nova_imagem.append((r, g, b, a))

img.putdata(nova_imagem)

# Recorta as bordas vazias ao redor da logo para ela ficar maior e mais nítida
bbox = img.getbbox()
if bbox:
    img = img.crop(bbox)

# Salva em PNG (formato que suporta transparência)
img.save("Tech-HOME.png", "PNG")
print("Logo sem fundo salva como Tech-HOME.png!")