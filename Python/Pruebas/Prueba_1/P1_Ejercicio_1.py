sArt = input("ingrese el nombre del articulo: ")
iPrec = int(input("Ingrese el valor unitario del articulo: "))
iCant = int(input("Ingrese cuantas unidades compro: "))

#IVA 15%

iPrecVent= iPrec * iCant
iPrecBru = iPrecVent + (iPrecVent * 0.15)

if iPrecBru > 1_000:
    iPrecBru = iPrecBru - (iPrecBru * 0.05)

print(f"FACTURA DE VENTA \n"
      f"Nombre del articulo: {sArt}\n"
      f"Precio del articulo: {iPrec:,.0f}\n"
      f"Cantidad de articulo: {iCant}\n"
      f"Precio de venta (sin IVA): {iPrecVent:,.0f}\n"
      f"Precio bruto (con IVA): {iPrecBru:,.2f}")
