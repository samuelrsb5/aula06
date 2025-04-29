A = [5,6,7,8,9]

M = [0]*5 #array dos multiplicados vazio
multiplicador = int(input("Informe um multiplicador inteiro: "))

for x in range(len(A)): #acesso à cada espaço do array
    M[x] = A[x] * multiplicador #atribui ao M o valor de cada INDICE do A multiplicado

print(A)
print(multiplicador)
print(M)