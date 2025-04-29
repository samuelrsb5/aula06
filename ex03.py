nomes = ["joao", "carlos", "maria", "luiza", "isabel"]

nomeDigitado = input("Digite um nome da lista: ")

mensagem = "Este nome não está na lista" #Utilize uma mensagem padrão sem estar presa a condições

for x in range(len(nomes)):
    if nomeDigitado == nomes[x]:
        mensagem = f"Achei o nome {nomeDigitado} na posição {x}"
        break

print(mensagem)