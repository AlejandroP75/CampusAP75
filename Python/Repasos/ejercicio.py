import json

ven = {}

with open("ventasssssss.txt")as archivo:
    ventas = archivo.readlines()

ventas.pop(0)
ven["vendedores"] = []

for vendedor in ventas:
    stralis = vendedor.rstrip().split(", ")
    ven["vendedores"].append({
        "Apellido":stralis[0],
        "Id":stralis[1],
        "Ventas":stralis[2:],
    })   
    
with open("vendedores.json", "w") as archivo:
    json.dump(ven, archivo, indent = 4)


