# for par in range(2, 101, 2):
#     print(par, end=",")


# dat = int(input("Ingrese el numero: "))
# fac = 1
# for i in range(1, dat+1):
#     fac = fac * i
    
# print(fac)

iNum = int(input("Ingrese el numero para saber si es primo o no: "))

prim = "sí"
culpable = 1
for i in range(2, iNum):
    if iNum % i == 0:
        prim = "no"
        culpable = i
        print(f"El numero {iNum} no es primo, el que lo divide es: {culpable}")

if prim != "no":
    print(f"El numero {iNum} es primo")


