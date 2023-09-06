import io

fd = open("mbox-short.txt", "r", encoding = "utf-8")

cont = 0
for linea in fd:
    cont += 1
fd.close()

print(f"La cantidad de lineas son: {cont}")