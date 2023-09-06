import json

midic = {1:"Lapiz", 2:"Borrador", 3:"Cuaderno", 4:"Lapiz", "valor":2500}

with open("jsonDic.json", "w") as archivo:
    json.dump(midic, archivo)
    print("Se ha escrito en disco")

if not archivo.closed:
    print("Cerrando archivo")
    archivo.close()

print("Se ha cerrado el archivo")