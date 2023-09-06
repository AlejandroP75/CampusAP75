import json

with open("jsonDic.json", "r") as archivo:
    midic = json.load(archivo)

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Diccionario", midic)
print("El valor del lapiz es", midic["valor"])