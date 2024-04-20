from tkinter import filedialog
from time import sleep
from os import path
import email.message
import smtplib

NovoU = " "
indice = 0
users = ' '
dirpath = filedialog.askdirectory()


# Verifica se o novo usuario já existe no sistema se existir retorna 1
def NovoUsu():
    with open(path.join (dirpath, "listaUsu.txt"), "r", encoding="utf-8") as usuarios:
        users = usuarios.readlines()
    for linha in users:

        if NovoU in linha:
            return 1
        
        
# Verifica se o usuario existe no sistema e retorna a posição dele na lista
def Veirficacao():
    with open(path.join (dirpath, "listaUsu.txt"), "r", encoding="utf-8") as usuarios:
        users = usuarios.readlines()
        cuz = 0
    for linha in users:
        cuz += 1
        if NovoU in linha:
            return cuz -1

# Manda a senha do Usuario para o email dele
def RecuperarSenha():
    corpo_email = f"""
    <h1>Olá {users[indice]}</h1>
    <p>Sua senha é {senhas[indice]}<p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = f"Recuperação de senha {users[indice]}"
    msg['From'] = "Email aqui"
    msg['To'] = Gmail
    password = "Senha dos app aqui"
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"],[msg["To"]], msg.as_string().encode('utf-8'))
    print("Email Enviado")




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
    print("[ 3 ] Fazer o login")
    print("[ 4 ] Recuperar a senha")
    print("*"*30)
    escolha  = str(input("Digite sua ação: "))
    if escolha == "0": # Criação de um novo usuario
        sleep(0.2)
        while True:
            with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
                users = usuarios.readlines()
            NovoU = (str(input(f"\n[ 0 ] Para parar | Usuarios registrado: {len(users)-1}\nDigite o nome de usuario: ")).strip())
            if NovoU == "0":
                break
            va = NovoUsu()
            if va == 1:
                print("\nUsuario já existente!!\n")
                indice = Veirficacao() 
                print(indice)
            else:
                senha = input("Digite sua senha: ").strip()
                with open(path.join (dirpath, "listaUsu.txt"), "a")as username:
                    username.write(f"\n{NovoU}")
                with open(path.join (dirpath, "listaSen.txt"), "a") as SenhaN:
                    SenhaN.write(f"\n{senha}")
                    sleep(0.5)
                    print("\nUsuario salvo")

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
    
    elif escolha == "3": # Login
        while True:
            with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
                users = usuarios.readlines()
            with open(path.join (dirpath, "listaSen.txt"), "r") as sen:
                senhas = sen.readlines()
            while True:
                NovoU = (str(input("Digite o nome de usuario: ")).strip())
                indice = Veirficacao() 
                if indice == 0:
                    print("\nUsuario Não existente!!\n")
                else:
                    SenhaConfir = (str(input(f"\nDigite sua senha: ")).strip())
                    if NovoU in users[indice] and SenhaConfir in senhas[indice]:
                        print("Login feito")
                    else:
                        print("Senha incorreta!!\n")
                        
    elif escolha == "4":   # Recuperar a senha
        
        with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
                users = usuarios.readlines()
        with open(path.join (dirpath, "listaSen.txt"), "r") as sen:
                senhas = sen.readlines()
        while True:              
                NovoU = (str(input(f"Digite o nome de usuario: ")).strip())
                indice = Veirficacao() 
                if indice == 0:
                    print("\nUsuario Não existente!!\n")
                else:
                    Gmail = (str(input(f"Digite seu email: ")).strip())
                    RecuperarSenha()
                    break
                    
    
    else:
        sleep(0.2)
        print("\n\nEscolha uma opção valida!!\n\n")
