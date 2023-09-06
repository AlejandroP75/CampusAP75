iDis = int(input("Ingrese las distancia a recorrer en kilometros: "))
iDia = int(input("Ingrese el numero de dias de su estancia: "))

iPrecioKm = 2_500

if iDia > 7 and iDis > 800:
    iPrecioKm = 2_500 - (2_500 * 0.3)

iPrecioTick = iPrecioKm * iDis

print(f"Numero de kilometros: {iDis}\n"
      f"Numero de dias: {iDia}\n"
      f"Precio del billete de ida y vuelta: {iPrecioTick:,.0f}")