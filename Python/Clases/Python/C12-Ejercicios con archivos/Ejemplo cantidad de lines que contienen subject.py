import io

fd = open("mbox-short.txt", "r", encoding = "utf-8")

cont = 0
for linea in fd:
    line = linea.rstrip()
    if not "@uct.ac.za" in line:
        cont += 1
        continue
    print(line)

fd.close()

print(f"La cantidad de lineas que empiezan con From: {cont}")