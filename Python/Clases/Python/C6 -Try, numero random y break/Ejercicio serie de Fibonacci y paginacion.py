
iA = 0
iB = 1
iSum = 1
iCont = 1
iDec = 0

print("-" * 70)
print("Los primeros 5 numeros de la serie de fibonacci son:")

while(iCont <= 5):
    iCont += 1
    print(iA, end=" ")
    iA = iB
    iB = iSum
    iSum = iA + iB

iDec = input("\nSi quiere continuar con la serie, digite el numero 1: ")
iCont = 0

if iDec == "1":
    while(iCont <= 4):
        iCont += 1
        print(iA, end=" ")
        iA = iB
        iB = iSum
        iSum = iA + iB
else:
    print("FIN DEL PROGRAMA")  
    print("-" * 30) 
