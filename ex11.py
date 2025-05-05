nums = [0]*10
contador = 0

for x in range(len(nums)):
    nums[x] = int(input("Digite números: "))

numeroQualquer = int(input("Digite um número inteiro: "))

for j in range(len(nums)):
    if nums[j] == numeroQualquer:
        contador = contador + 1

print(contador)