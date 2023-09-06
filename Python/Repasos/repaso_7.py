import json

with open("Campus-main/Repasos/Ahorradores.json") as file:
    ahorradores = json.load(file)

dian = []
cont = 1
for datos in ahorradores["cliente"]:
    if datos["Saldo"] > 35000000:
        dian.append({
            "Consecutivo":cont,
            "numCuenta": datos["NumCuenta"],
            "Saldo":datos["Saldo"]
        })
        cont += 1 
    

with open("Dian.json", "w") as file:
    json.dump(dian, file, indent = 4)

