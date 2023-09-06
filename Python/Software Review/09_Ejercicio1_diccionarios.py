def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

articulos = {1:"Lapices",2:"Cuadernos",3:"Borradores",4:"Calculadoras",5:"Escuadras"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}
valoresCom = {1:0, 2:0, 3:0, 4:0, 5:0}
cantidadCom = {1:0, 2:0, 3:0, 4:0, 5:0}
valorT = 0
     
while True:    
    while True:    
        codigo = leerInt("Ingrese el codigo del articulo: ")
        if codigo < 1 or codigo > 5:
            print("Ingrese un numero del 1 al 5")
            continue
        break
    
    cantidad = leerInt("Ingrese la cantidad de articulos que desea comprar: ")
    cantidadCom[codigo] = cantidad
    valorU = valores[codigo]*cantidadCom[codigo]
    valoresCom[codigo] = valorU
    valorT = valorT + valorU
    
    print("_" * 75)
    opc= input("Desea comprar algo mas (s/n)? ")
    if opc.lower() == "n":
        break
    
print("_" * 75)
for k in articulos.keys():
    print(f"{articulos[k]}:\tValor unitario: {valores[k]:,.0f}\tCantidad comprada: {cantidadCom[k]}\t Total: {valoresCom[k]:,.0f}")   
print(f"\nEl valor total de su compra fue: ${valorT:,.0f}")
