userName = [""]*5
userPassword = [""]*5
inputUser = [""]
inputPass = [""]

for x in range(5):
    userName[x] = input("Digite nomes: ")

for j in range(5):
    userPassword[j] = input("Digite senhas: ")

for y in range(1):
    inputUser[y] = input("Digite um usuário: ")

for z in range(1):
    inputPass[z] = input("Digite uma senha: ")

for i in range(1):
    if inputUser[i] == userName[i] and inputPass[i] == userPassword[i]:
        print(f"Login efetuado com sucesso, bem vindo {userName[i]}")