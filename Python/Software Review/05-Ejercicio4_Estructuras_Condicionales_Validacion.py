bCiclo = False

while bCiclo == False:
    print("-" * 75)
    sContr = input("Ingrese una contraseña: ")
    iLong = len(sContr)
    iMayMen = sContr.swapcase()
    iNum = 0
    iEspa = 0
    iEspe = 0
    if(iLong >= 8):
        if iMayMen != sContr.upper() and iMayMen != sContr.lower():
            for i in range(1, iLong):

                if sContr[i].isdigit() == True:
                    iNum += 1

                if sContr[i] == " ":
                    iEspa += 1

                if sContr[i] == "%" or sContr[i] == "&" or sContr[i] == "":
                    iEspe += 1
            if iNum > 0:
                if iEspa == 0:
                    if iEspe > 0:
                        bCiclo= True
                    else:
                        print("-" * 75)
                        print("No cumple los requisitos, la contraseña no contiene caracter especial")
                else:
                    print("-" * 75)
                    print("No cumple los requisitos, la contraseña no tiene espacios")
            else:
                print("-" * 75)
                print("No cumple los requisitos, la contraseña no tiene por lo menos un numero")         
        else:
            print("-" * 75)
            print("No cumple los requisitos, la contraseña no tiene al menos una minuscula y una mayuscula")
    else:
        print("-" * 75)
        print("No cumple los requisitos, la contraseña tiene menos de 8 digitos")

    if bCiclo == True:
        print("-" * 75)
        print("Su contraseña ha sido guardada")
        print("Fin del programa")