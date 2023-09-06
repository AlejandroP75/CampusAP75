#break, rompe el ciclo

# for i in range (1, 10):
#     print (i, end=",")
#     if i == 5:
#         break
# print("Fin del programa")

#continue, todo lo que este debajo del continue lo salta
#y empieza el siguiente ciclo

# for i in range (1, 10):

#     if i == 5:
#         continue
#     print (i, end=", ")

# print("\nFin del programa")

while True:
    try:
        
        iNum = int(input("Ingrese un numero: "))
        
        if iNum < 2:
            print("Ingrese un numero entero mayor que uno.")
            continue
        break
    except ValueError:
        print("Ingrese un numero valido.")