import json


def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("\nIngrese un numero entero valido")

def leerFloat(msg):
    while True:
        try:
            iNum = float(input(msg))
            return iNum
        except ValueError:
            print("\nIngrese un numero decimal valido")

jugadores = {}
num = 1

while True:
    nom = input("\nIngrese el nombre del jugador: ")
    if nom.strip() == "":
        break
    eda = leerInt("\nIngrese la edad del jugador: ")
    pes = leerFloat("\nIngrese el peso del jugador: ")
    jugadores[num] = {
        "Nombre":nom,
        "Edad":eda,
        "Peso":pes}
    op = input("\nDesea añadir los datos de otro jugador?(s/n): ")
    if op.lower() == "s":
        num = num + 1
        continue
    break

with open("Jugadores.json", "w") as file:
    json.dump(jugadores, file, indent = 4)

print("\nDatos guardados en el json")