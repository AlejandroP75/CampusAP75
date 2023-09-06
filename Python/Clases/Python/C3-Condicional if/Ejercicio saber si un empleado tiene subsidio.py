sNom = input("Ingrese el nombre del empleado: ")
iSal = int(input("Ingrese el salario del empleado: "))

if iSal <= 1_200_000:
    iSubTrans = 120_000
else:
    iSubTrans = 0

print(f"Nombre: {sNom}\n"
      f"Salario: {iSal:,.0f}\n"
      f"Subsidio de transporte: {iSubTrans:,.0f}".replace(",", ".")) 
