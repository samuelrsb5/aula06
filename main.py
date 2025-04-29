# arrayCompras = ['banana', 'laranja', 'maçã']
#
# for i in arrayCompras:
#     print(i)
#
#
# #ou
#
#
# for i in range(len(arrayCompras)):
#     print(arrayCompras[i]


nome = [""]*5 #lista vazia com 5 espaços
nome.append("Joao") #adiciona um valor na ultima posição do array
nome[1] = "Carlos" #insere no local escolhido definindo na variável
nome.insert(0, "Pitbull do samba") #insere no local escolhido
nomeA = nome.pop(0) #remove o item da lista e pode ser atribuido a uma variavel
print(nomeA)
print(nome)


nome = {
    "nome": "nota"
}

