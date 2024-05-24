from tkinter import filedialog
from time import sleep
from os import path
import email.message
import smtplib

NovoU = " "
indice = 0
users = ' '
Emails = ' '
dirpath = filedialog.askdirectory()

# Verifica se o novo usuario já existe no sistema se existir retorna 1
def NovoUsu():
    with open(path.join (dirpath, "listaUsu.txt"), "r", encoding="utf-8") as usuarios:
        users = usuarios.readlines()
    for linha in users:
        if NovoU in linha:
            return 1
    return 0
        
        
# Verifica se o usuario existe no sistema e retorna a posição dele na lista
def Veirficacao():
    with open(path.join (dirpath, "listaEmail.txt"), "r", encoding="utf-8") as emai:
       Emails = emai.readlines()
    for linha in Emails:
        if Gmail in linha:
            return 1
    return 0

# Mande um email para o usuario
def MandarEmail():
    corpo_email = f"""
    <h1>Olá {users[indice]}</h1>
    
    """
    
    msg = email.message.Message()
    msg['Subject'] = f"Mensagem automatica, não responder {users[indice]}"
    msg['From'] = "Seu email aqui"
    msg['To'] = Gmail
    password = "Sua senha de app aqui"
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"],[msg["To"]], msg.as_string().encode('utf-8'))
    print("Email Enviado")




 # Criação dos arquivos base
escolha = str(input("Deseja resetar/criar novos arquivos de Usuarios e Emails? [1] sim  "))
if escolha == "1":
    with open(path.join (dirpath, "listaUsu.txt"), "w") as usuarios:
        usuarios.write("Usuarios")
    with open(path.join (dirpath, "listaEmail.txt"), "w") as emai:
        emai.write("Emails")

while True:

    print("*"*30)
    print("[ 0 ] Registrar novo usuario ")
    print("[ 1 ] Mostrar usuarios")
    print("[ 2 ] Mandar um email")
    print("[ 3 ] Finalizar programa")
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
                email = input("Digite seu email: ").strip()
                with open(path.join (dirpath, "listaUsu.txt"), "a")as username:
                    username.write(f"\n{NovoU}")
                with open(path.join (dirpath, "listaEmail.txt"), "a") as emails:
                    emails.write(f"\n{email}")
                    sleep(0.5)
                    print("\nUsuario salvo")

    elif escolha == "1": # Ler todos os usuarios criados
        with open(path.join (dirpath, "listaUsu.txt"), "r") as usuarios:
             users = usuarios.readlines()
        with open(path.join (dirpath, "listaEmail.txt"), "r") as emai:
            emai = emai.readlines()
        sleep(0.2)
        print("Aguarde...")
        sleep(1.5)
        for c in range(len(users)): # Mostar todos os usuarios criados
            print(f"\nUsuario: {users[c]} | Email: {emai[c]}\n")
        
  
                        
    elif escolha == "2":   # Mandar um email
        Gmail = (str(input(f"Digite seu email: ")).strip())
        va = Veirficacao()
        if va == 1:
            MandarEmail()
        else:
            print("Email não encontrado")

                    
    elif escolha == "3": # Finalizar o programa
        sleep(0.2)
        print("\nFinalizando programa...\n")
        sleep(1)
        break 
    
    else:
        sleep(0.2)
        print("\n\nEscolha uma opção valida!!\n\n")
