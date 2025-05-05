num = int(input("Digite um número: "))

A = [0]*num
B = [0]*num

for i in range(num):
    A[i] = int(input("Digite A: "))

for j in range(num):
    B[j] = int(input("Digite B: "))

for x in range(num):
    soma = A[x] + B[x]

