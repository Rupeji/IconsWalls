import os

carpeta = "Wallpapers"
exts = (".jpg", ".jpeg", ".png", ".webp")
imgs = sorted([f for f in os.listdir(carpeta) if f.lower().endswith(exts)])

lineas = ["# Mis Wallpapers\n\n", "| | | |\n", "| :---: | :---: | :---: |\n"]

for i in range(0, len(imgs), 3):
    fila = []
    for img in imgs[i:i+3]:
        ruta = f"{carpeta}/{img}"
        fila.append(f"![{img}]({ruta})")
    while len(fila) < 3:
        fila.append(" ")
    lineas.append("| " + " | ".join(fila) + " |\n")

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lineas)
