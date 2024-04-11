from tkinter import filedialog
from time import sleep
from os import path

NovoU = " "
users = ' '
dirpath = filedialog.askdirectory()

# Verifica se o novo usuario já existe no sistema se existir retorna 1
def NovoUsu():
    with open(path.join (dirpath, "listaUsu.txt"), "r", encoding="utf-8") as usuarios:
        users = usuarios.readlines()
    for linha in users:
        if NovoU in linha:
            return 1

 # Criação dos arquivos base
escolha = str(input("Deseja resetar/criar novos arquivos de Usuarios e senhas? [1] sim  "))
if escolha == "1":
    with open(path.join (dirpath, "listaUsu.txt"), "w") as usuarios:
        usuarios.write("Usuarios")
    with open(path.join (dirpath, "listaSen.txt"), "w") as senhas:
        senhas.write("Senha")

while True:

    print("*"*30)
    print("[ 0 ] Registrar novo usuario ")
    print("[ 1 ] Mostrar usuarios")
    print("[ 2 ] Finalizar programa")
    print("*"*30)
    escolha  = str(input("Digite sua ação: "))
    if escolha == "0": # Criação de um novo usuario
        sleep(0.2)
        while True:
            with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
                users = usuarios.readlines()
            NovoU = (str(input(f"[ 0 ] Para parar | Usuarios registrado: {len(users)-1}\nDigite o nome de usuario: ")).strip())
            if NovoU == "0":
                break
            va = NovoUsu()
            if va == 1:
                print("\nUsuario já existente!!\n")
            else:
                senha = input("Digite sua senha: ")
                with open(path.join (dirpath, "listaUsu.txt"), "a")as username:
                    username.write(f"\n{NovoU}")
                with open(path.join (dirpath, "listaSen.txt"), "a") as SenhaN:
                    SenhaN.write(f"\n{senha}")

    elif escolha == "1": # Ler todos os usuarios criados
        with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
             users = usuarios.readlines()
        with open(path.join (dirpath, "listaSen.txt"), "r") as sen:
            senhas = sen.readlines()
        sleep(0.2)
        print("Aguarde...")
        sleep(1.5)
        for c in range(len(users)): # Mostar todos os usuarios criados
            print(f"\nUsuario: {users[c]} | Senha: {senhas[c]}\n")
        
    elif escolha == "2": # Finalizar o programa
        sleep(0.2)
        print("\nFinalizando programa...\n")
        sleep(1)
        break
    
    else:
        sleep(0.2)
        print("\n\nEscolha uma opção valida!!\n\n")
                     