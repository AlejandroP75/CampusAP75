iN1 = int(input("Ingrese el primer numero: "))
iN2 = int(input("Ingrese el segundo numero: "))

iCon1 = 0
iCon2 = 0
for i in range(1, iN1):
    if iN1 % i == 0:
        iCon1 = iCon1 + i

for h in range(1, iN2):
    if iN2 % h == 0:
        iCon2 = iCon2 + h

if iN1 == iCon2 and iN2 == iCon1:
    print(f"Los numeros {iN1} y {iN2} son amigos")
else:
    print(f"Los numeros {iN1} y {iN2} no son amigos")