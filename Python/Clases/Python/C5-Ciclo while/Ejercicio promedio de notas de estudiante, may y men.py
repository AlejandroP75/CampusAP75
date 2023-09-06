iCic = 1
iProm = 0
fPromNot = 0
fNotMay = 0
fNotMen = float("Inf")

print("-" * 50)
print("Bienvenido, porgrama que le dice el promedio de las notas de los estudiantes, tanto como quien saco la mayor nota y quien la menor,\n"
      "si terminó de ingresar los estudiantes por favor escriba FIN para mostrar los resultados")

while iCic != 0:
    print("-" * 50)
    sNom = input("Ingrese el nombre del estudiante: ")
    if sNom != "FIN":
        fNot = float(input("Ingrese la nota del estudiante: "))

        fPromNot = fPromNot + fNot
        iProm = iProm + 1

        if fNot > fNotMay:
            fNotMay = fNot
            sEstMay = sNom
    
        if fNot < fNotMen:
            fNotMen = fNot
            sEstMen = sNom
    else:
        iCic = 0

fPromCur = fPromNot / iProm

print("-" * 50)
print(f"El promedio del curso fue de: {fPromCur:,.2f}\n"
      f"El estudiante con la mayor nota fue {sEstMay} con una nota de {fNotMay}\n"
      f"El estudiante con la menor nota fue {sEstMen} con una nota de {fNotMen}")


