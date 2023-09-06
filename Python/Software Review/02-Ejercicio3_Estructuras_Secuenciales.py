iValorHora = 20000
iHorasTrabajadas = 8

iSueldoBruto = (iValorHora * iHorasTrabajadas)
fValorEPS = (iSueldoBruto * 0.04)
fValorPension = (iSueldoBruto * 0.04)
iSueldoNeto = iSueldoBruto - fValorEPS - fValorPension

print(f"Sueldo bruto: {iSueldoBruto:,.0f}\n"
      f"Descuento por EPS: -{int(fValorEPS):,.0f}\n"
      f"Descuento por pension: -{int(fValorPension):,.0f}\n"
      f"Sueldo neto: {int(iSueldoNeto):,.0f}\n".replace(",", "."))