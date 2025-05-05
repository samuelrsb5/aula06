nomes = ["", "", "", "", ""]

for x in range(len(nomes)):
    nomes[x] = input("digite nomes: ")

for i in range(len(nomes)):
    print(nomes[i])

print("-----")

#tambem da pra usar o -1 para distancia de percorrimento do array!!!
for j in range(4, -1, -1):
    print(nomes[j])

