import io

fd = open("mbox-short.txt", "r", encoding = "utf-8")

cont = 0
for linea in fd:
    if linea.startswith("From"):
        cont += 1
fd.close()

print(f"La cantidad de lineas que empiezan con From: {cont}")