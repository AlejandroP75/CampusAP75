sNombre = "Pedro"
sPlaca = "JNP080"
iValorPasaje = 10000
iValorEncomienda = 15000

fPagoPasaje = iValorPasaje * 0.25
fPagoEncomienda = iValorEncomienda * 0.15
fSueldoConductor = (fPagoPasaje) + (fPagoEncomienda)

print(f"Conductor: {sNombre}\n"
      f"Placa: {sPlaca}\n"
      f"Valor total pasajes: {iValorPasaje:,.0f}\n"
      f"Valor a pagar por pasajes: {int(fPagoPasaje):,.0f}\n"
      f"Valor total encomiendas: {iValorEncomienda:,.0f}\n"
      f"Valor a pagar por encomiendas: {int(fPagoEncomienda):,.0f}\n"
      f"Valor total a pagar: {int(fSueldoConductor):,.0f}".replace(",", "."))