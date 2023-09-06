#(i += 1) == (i + i = 1)
try:
    print("-" * 70)
    iNum = int(input("Ingrese un numero: "))
    iResu = 10 / iNum
    print(f"El resultado de la operacion es: {iResu:,.0f}")
except ValueError:
    print("Debes ingresar un numero valido, por favor vuelve a intentar.")
except ZeroDivisionError:
    print("El numero no puede ser igual a 0, por favor vuelve a intentar.")
except Exception as e:
    print("Hubo un error inesperado, por favor vuelve a intentar" , str(e))

print("Fin.")
print("-" * 70)
