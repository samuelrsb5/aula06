userName = [""]*5
userPassword = [""]*5

for x in range(5):
    userName[x] = input("Digite nomes: ")

for j in range(5):
    userPassword[j] = input("Digite senhas: ")

for y in range(5):
    print(f"{y} - Usuário: {userName[y]} | Senha: {userPassword[y]}")

