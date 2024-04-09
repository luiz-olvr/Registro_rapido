listaU = []
listaS = []
NovoU = " "
val = 0

def NovoUsu():
    with open("listaUsu.txt", "r", encoding="utf-8") as usuarios:
        users = usuarios.readlines()
        print(users)
    for linha in users:
        if NovoU in linha:
            return 1



escolha = input("Deseja resetar/criar novos arquivos de Usuarios e senhas? [1] sim  ")
if escolha == 1:
    with open("listaUsu.txt", "w") as usuarios:
        usuarios.write("Usuarios")
    with open("listaSen.txt", "w") as senhas:
        senhas.write("Senha")

while True:
    if val == 1:
        print("login aprovado")
        break
    print("*"*30)
    print("[ 0 ] Registrar novo usuario ")
    print("[ 1 ] Logar")
    print("[ 2 ] Mostrar usuarios")
    print("*"*30)
    escolha  = int(input("Digite sua ação: "))
    if escolha == 0:
        NovoU = (str(input("Digite o nome de usuario: ")).strip())
        va = NovoUsu()
        if va == 1:
            print("\nUsuario já existente!!\n")
        else:
            senha = input("Digite sua senha: ")
            with open("listaUsu.txt", "a")as username:
                username.write(f"\n{NovoU}")
            with open("listaSen.txt", "a") as SenhaN:
                SenhaN.write(f"\n{senha}")
    if escolha == 1:
        nome = str(input("Digite seu usuario: ")).strip()
        senha = str(input("Digite sua senha: ")).strip()
        for c in range(len(listaS)):
            if nome == listaU[c] and senha == listaS[c]:
                val = 1
                break
    if escolha == 2:
        with open("listaUsu.txt", "r") as usuarios:
             users = usuarios.readlines()
        with open("listaSen.txt", "r") as sen:
            senhas = sen.readlines()
       
        for c in range(len(users)):
            print(f"\nUsuario: {users[c]} | Senha: {senhas[c]}\n")
       # users usuarios.readlines()
""" for c in range(len(listaS)):
            print(f"\nUsuario: {listaU[c]}, Senha: {listaS[c]}")"""


