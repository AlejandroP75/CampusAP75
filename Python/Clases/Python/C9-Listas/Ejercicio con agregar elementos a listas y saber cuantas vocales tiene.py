def leerInt(msg):
    while True:
        try:
            print("_" * 75)
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

letras = []


limNum = leerInt("Ingrese el numero de letras que va a digitar: ")
for i in range(limNum):
    while True:
        letra = input(f"Ingrese la letra {i+1}: ")
        if len(letra) != 1:
            print("Ingrese solo una letra a la vez")
            continue
        break
    letra = letra.upper()
    letras.append(letra)

sA = letras.count("A")
sE = letras.count("E")
sI = letras.count("I")
sO = letras.count("O")
sU = letras.count("U")

print("_" * 50)
print(f"\nLas letras ingresadas son: {letras}"
      f"\n\nEl numero de letras a es: {sA}" 
      f"\n\nEl numero de letras e es: {sE}" 
      f"\n\nEl numero de letras i es: {sI}" 
      f"\n\nEl numero de letras o es: {sO}" 
      f"\n\nEl numero de letras u es: {sU}")           




