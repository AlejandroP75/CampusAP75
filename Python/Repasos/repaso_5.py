import json

data = {}
data["clients"] = []

data["clients"].append({
    "first_name":"Theodoric",
    "last_name":"Rivers",
    "age":36,
    "amount":1.11
})

data["clients"].append({
    "first_name":"Pedro",
    "last_name":"Sanchez",
    "age":55,
    "amount":5.7
})

with open("data.json", "w") as file:
    json.dump(data, file, indent = 4)