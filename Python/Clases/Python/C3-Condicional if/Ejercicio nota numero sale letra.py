sNom = input("Ingrese el nombre del estudiante: ")
iNot = int(input("Ingrese la calificación del estudiante: "))

if iNot >= 0 and iNot <= 59:
    sCal = "D"
elif iNot >= 60 and iNot <= 79:
    sCal = "C"
elif iNot >= 80 and iNot <= 89:
    sCal = "B"
else:
    sCal = "A"

print(f"Nombre: {sNom}\n"
      f"Calificación cuantitativa: {iNot}\n"
      f"Calificación cualitativa: {sCal}")
