fd = open("prueba_2.txt", "w")
lst = ["Primera linea\n", "Segunda linea\n"]
fd.writelines(lst)
fd.close()