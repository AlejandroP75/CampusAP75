print("Bienvenido al programa que le mostrara los numeros divisibles entre 3 y 7, del 1 al 1000")

for i in range (1, 1001):
    if i % 3 == 0:
        print(f"El numero {i} es divisible entre 3")
        if i % 7 == 0:
            print(f"El numero {i} es divisible entre 7")
    