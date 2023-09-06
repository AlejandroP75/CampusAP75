import random

iGan = 0
sMejorJug = ""
iContMeJu = float("Inf")
iPerd = 0

while True:
    try:
        print("-" * 70)
        iNumJug = int(input("Bienvenido al juego de tratar de adivinar lo mas pornto posible el numero que penso la computadora\nIngresa el numero de jugadores: "))
        break
    except ValueError:
        print("Ingrese un numero valido")
    except Exception as e:
        print("Hubo un error inesperado, por favor vuelve a intentar" , str(e))

for i in range (iNumJug):
    iRan = random.randrange(1, 101)
    iNumInt= random.randrange(3, 6)
    print("-" * 75)
    sNomJug = input(f"Ingrese el nombre del jugador {i + 1}: ")
    iCont = 1
    while iGan == 0:
        #Verificacion de numero ingresado valido
        while True:    
                try:
                    print("-" * 75)
                    iNum = int(input("Trate de adivinar el numero que pensara la computadora, ingrese un numero del 1 al 100: "))
                    if iNum < 0 or iNum > 100:
                        print("Por favor ingrese un numero entre el 1 y el 100")
                        continue
                    break
                except ValueError:
                    print("Ingrese un numero valido")
                except Exception as e:
                    print("Hubo un error inesperado, por favor vuelve a intentar" , str(e))
        #Comparacion para dar pistas y alerta de victoria
        if iCont == iNumInt:
            print(f"Tu numero de intentos era {iNumInt}, asi que perdiste")
            iPerd += 1
            break
        if iNum == iRan:
            print(f"Felicidades has acertado, te ha tomado este numero de intentos: {iCont}")
            break
        elif iNum > iRan:
            print("Ufff intenta con un numero menor")
        else:
            print("Ufff intenta con un numero mayor")
        iCont += 1

    if iCont < iContMeJu:
        sMejorJug = sNomJug
        iContMeJu = iCont
    
        if iPerd == iNumJug and iPerd > (iNumJug - 1):
            print("-" * 75)
            print("Ninguno de los jugadores acerto el numero en su numero de intentos. No hay ganador\n"
                "FIN DEL PROGRAMA")
            print("-" * 75)
        elif iPerd < iNumJug:
            print("-" * 75)
            print(f"Jugador ganador: {sMejorJug} \nNumero de intentos: {iContMeJu}\n"
                 "Felicidades\n"
                 "FIN DEL PROGRAMA")   
            print("-" * 75)