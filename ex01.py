nomes = [""]*5 #crio o array com 5 espaços vazios

for x in range(len(nomes)): #crio um for utilizando o tamanho do array como limite
    nomes[x] = input("Digite um nome: ") #atribuo o valor digitado ao indice X a cada loop

print(nomes)