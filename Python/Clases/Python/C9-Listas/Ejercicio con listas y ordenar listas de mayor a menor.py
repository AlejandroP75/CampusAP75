def leerFloat(msg):
    while True:
        try:
            print("_" * 75)
            iNum = float(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero flotante valido")

listaEstudiantes = []

for i in range(10):
    while True:
        nota = leerFloat(f"Ingrese nota estudiante {i+1}: ")
        if nota < 0 or nota > 5.0:
            print("El valor de la nota debe ser de 0.0 a 5.0")
            continue
        listaEstudiantes.append(nota)
        break

notMen = min(listaEstudiantes)
print("_" * 70)
print(f"\nLa nota menor es: {notMen}")
notMay = max(listaEstudiantes)
print(f"La nota mayor es: {notMay}")

promNotas = sum(listaEstudiantes) / 10
print(f"La promedio de las notas es: {promNotas}")

listaEstudiantes.sort(reverse = True)
tresNotas = listaEstudiantes[0:3]
print(f"Las tres mejores notas son: {tresNotas}")

    
