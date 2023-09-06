print("Programa para calcular el siguiente numero de la serie")
i = 1
print(1)
print(1)
for au in range(2):
    if au == 1:
        print("-"*50)
        print(f"El siguiente numero de la series es: {i}")
        print ("La serie continua con: ")
    i = i + 1
    print(f"{i}, ")
    i = i - 3
    print(f"{i}, ")
    i = i + 2
    print(f"{i}, ")
    i = i - 3
    print(f"{i}, ")

