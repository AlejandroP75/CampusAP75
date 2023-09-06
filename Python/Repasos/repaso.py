dicContact = {}
while True:
    while True:
        while True:
                try:
                    sNom = input("\nIngrese su nombre de usuario: ")
                    if sNom.strip() == "":
                        print("\nPor favor ingrese un nombre valido")
                        continue
                    break
                except Exception as e:
                    print("\nError al ingresar un nombre" , e.message)
        if sNom in dicContact.keys():
            print("\nEste nombre ya esta registrado, introduzca uno diferente")
            continue
        break
    while True:
            try:
                while True:
                    iNum = int(input("\nIngrese el numero de telefono: "))
                    if len(str(iNum)) != 10:
                        print("\nEl numero de telefono debe tener 10 digitos, vuelva a ingresarlo")
                        continue
                    break
                break
            except ValueError:
                print("\nIngrese un numero de telefono valido")
    dicContact[sNom] = iNum
    op = input("\n¿Desea continuar (s/n)?: ")
    if op.upper() == "S":
        continue
    break
print("\nFIN DEL PROGRAMA\n")
print(dicContact)