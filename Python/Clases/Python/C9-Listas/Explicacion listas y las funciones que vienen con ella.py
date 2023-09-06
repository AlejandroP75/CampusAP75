def buscarElem(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i
    return -1    

def encontrarElem(lst, elem):
    for e in lst:
        if e == elem:
            return True
    return False   

miLista = []
miLista = list()

print(miLista, len(miLista))

miLista.append("Alirio")

print(miLista, len(miLista))

miLista.extend(["Andres", "Carlos", "Cristian" , "Diana"])
print(miLista, len(miLista))

miLista.pop() #Borra el ultimo elemento
print(miLista, len(miLista))

miLista.insert(2, "Lilian")
print(miLista, len(miLista))

miLista.remove("Carlos")
print(miLista, len(miLista))

#Recorrido por indice
for elem in range(len(miLista)):
    print(elem, "-->", miLista[elem])

#Recorrido por elementos
print("_" * 50)
for elem in miLista:
    print(elem)

#Buscar un elemento si esta devuelve la posicion y sino devuelve -1
pos = buscarElem(miLista, "Andres")
print(pos)

#Buscar un elemento en la lista, si esta, devuelve true, sino false
esta = encontrarElem(miLista, "Carlos")
print(esta)

#Metodo para borrar el contenido de una lista
miLista = []
