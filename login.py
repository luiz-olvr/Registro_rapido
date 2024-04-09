listaU = []
listaS = []
val = 0
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
        listaU.append(str(input("Digite o nome de usuario: ")).strip().capitalize())
        listaS.append(str(input("Digite sua senha: ")).strip())
    if escolha == 1:
        nome = str(input("Digite seu usuario: ")).strip().capitalize()
        senha = str(input("Digite sua senha: ")).strip()
        for c in range(len(listaS)):
            if nome == listaU[c] and senha == listaS[c]:
                val = 1
                break
    if escolha == 2:
        for c in range(len(listaS)):
            print(f"\nUsuario: {listaU[c]}, Senha: {listaS[c]}")

