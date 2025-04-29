nomes = [""]*5 #crio o array com 5 espaços vazios

for x in range(len(nomes)): #crio um for utilizando o tamanho do array como limite
    nomes[x] = input("Digite um nome: ") #atribuo o valor digitado ao indice X a cada loop


for j in range(len(nomes)): #NAO REAPROVEITAR VARIAVEIS DE FOR(NAO REPETIR X)
    print(nomes[x], j) #acessa o conteudo do array e sua posição, X = conteudo J = posição
