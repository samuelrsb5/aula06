#pedir 5 notas
#ler o array e fazer a média
#verificar no array quantas notas foram maior que a média

#OBS - O INDICE CHAMADO NO FOR PRECISA SER CORRESPONDENTE AOS USADOS DENTRO DELE
# SE SEU FOR USA J DE INDICE USE J EM OPERAÇÕES DENTRO DELE
# NAO REPITA INDICES EM FORS DIFERENTES
notas = [0.0]*5
soma = 0
contagemAcima = 0
for x in range(len(notas)):
    notas[x]= float(input("Digite notas: "))


for j in range(len(notas)):
    soma = soma + notas[j]


media = soma / len(notas)
for z in range(len(notas)):
    if notas[z] > media:
        contagemAcima = contagemAcima + 1

print(f"{contagemAcima} alunos ficaram acima da média {media}")
