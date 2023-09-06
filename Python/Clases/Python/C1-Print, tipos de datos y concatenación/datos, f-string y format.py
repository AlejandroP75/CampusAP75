numero1 = 10
numero2 = 1.124568
sNombre = "Oscar"
numero2 = "Daniel"
sw = False
numero2 = numero1 // 2
numero2 = numero2 ** 2 * 3 - 2
print(type(numero2))

# OPERADORES DE CADENA

"""
A continuacion se veran los
diferentes operadores de cadena
"""
str1 = "hola"
str2 = "mundo"
str3 = str1 + " " + str2
print(str3)

#Operador Repetición (*)
str3 = str1 * 3
print(str3)

# FORMATO DE CADENAS

# cadenas f-string
print(f"hola {str2} , {numero2}")

# cadenas con format
print("Hola %s , %d" % ("mundo", numero2))
