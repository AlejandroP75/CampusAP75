iVALORHORA= 20_000
print("-" * 50)
iUsu = int(input("Ingrese el numero de empleados: "))

iContSB = 0
iContSN = 0
iContEPS = 0
iContP = 0
iMen = 100000000000000
iMay = 0

for i in range(1, iUsu + 1):
    print("-" * 50)
    sNom = input("Ingrese el nombre del empleado: ")
    iHoras = int(input(f"Ingrese el numero de horas trabajadas del empleado: "))
    iSueldoBruto = (iVALORHORA * iHoras)
    iContSB = iContSB + iSueldoBruto
    fValorEPS = (iSueldoBruto * 0.04)
    iContEPS = iContEPS + fValorEPS
    fValorPension = (iSueldoBruto * 0.04)
    iContP = iContP + fValorPension
    iSueldoNeto = iSueldoBruto - fValorEPS - fValorPension
    iContSN = iContSN + iSueldoNeto
    print("-" * 50)
    print(f"Trabajador: {sNom}")
    print(f"Sueldo bruto: {iSueldoBruto:,.0f}\n"
      f"Descuento por EPS: -{int(fValorEPS):,.0f}\n"
      f"Descuento por pension: -{int(fValorPension):,.0f}\n"
      f"Sueldo neto: {int(iSueldoNeto):,.0f}\n".replace(",", "."))
    if iSueldoNeto < iMen:
        iMen = iSueldoNeto
        sNomMen = sNom
    elif iSueldoNeto > iMay:
        iMay = iSueldoNeto
        sNomMay = sNom
    iPromSB = iContSB / iUsu
    iPromSN = iContSN / iUsu
    
print("-" * 50)
print(f"Total salarios brutos = {iContSB:,.0f}\n"
      f"Total descuentos por EPS = {iContEPS:,.0f}\n"
      f"Total descuentos por pensión = {iContP:,.0f}\n"
      f"Total salarios netos = {iContSN:,.0f}")   
print("-" * 50)
print(f"El empleado con el mayor salario neto es {sNomMay} con {iMay:,.0f} de salario neto\n"
      f"El empleado con el menor salario neto es {sNomMen} con {iMen:,.0f} de salario neto")
print("-" * 50)
print(f"Promedio de salarios brutos = {iContSB:,.0f}\n"
      f"Promedio de salarios netos = {iContSN:,.0f}") 
 
