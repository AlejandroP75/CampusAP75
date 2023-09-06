tx = open("mbox-short.txt", "r")
emails = set()

for i in tx:
    if i.startswith("From: "):
        i = i[6:]
        emails.add(i)

send = list(emails)
for i in range(len(send)-1, 0, -1):
    i = send[i]
    j = print("Enviado OK\t", i.rstrip())
    
tx.close

fd = open("prueba_2.txt", "w")
fd.writelines(send)
fd.close()