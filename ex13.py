nums = [0]*5
soma = 0
contagemAcima = 0
for x in range(len(nums)):
    nums[x] = int(input("Digite numeros: "))

print("------")

maiores = nums[0]
menores = nums[0]

for j in range(len(nums)):
    if nums[j] % 2 == 0:
        print(nums[j])

print("------")

for i in range(len(nums)):
    if nums[i] > maiores:
        maiores = nums[i]
    elif nums[i] < menores:
        menores = nums[i]

#colocar o print fora, se não, vai repetir referente ao len do array
print(maiores)
print(menores)

print("------")


for y in range(len(nums)):
    soma = soma + nums[y]

media = soma / len(nums)
for z in range(len(nums)):
    if nums[z] > media:
        contagemAcima = contagemAcima + 1

print(f"{contagemAcima} estão acima da média do vetor")