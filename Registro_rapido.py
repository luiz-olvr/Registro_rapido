from os import path
from tkinter import filedialog
dirpath = filedialog.askdirectory()

criar = int(input("Deseja criar novos arquivos[ 0 ]?\nContinuar com os antigos[ 1 ]?\nEscolha: "))
if criar == 1:
    pass 

lista = list()

while True:
    print("""
          [ 0 ] adicionar um usuario
          [ 1 ] ver todos os usuarios
          [ 2 ] pesquisar usuario
          [ 3 ] deletar usuario
          [ 4 ] gerar arquivo de texto
          [ 5 ] encerrar programa
         """)
    esc = int(input("Digite a opção: "))
    if esc == 0:
        nome = str(input("Digite o nome do usuario: "))
        email = str(input("Digite o email: "))
        for c in range(0,len(lista)):
            if  nome in lista[c]['nome'] and email in lista[c]['email']:
                print("Usuario já existente!")
        lista.append({"nome": nome, "email": email})

    elif esc == 1:
        for c in range(0,len(lista)):
            print(f'\nUsuario : {lista[c]['nome']} \nEmail: {lista[c]['email']}\n')

    elif esc == 2:
        nome = str(input("Digite o nome do usuario: "))
        email = str(input("Digite o email: "))
        
        for c in range(0,len(lista)):
            if  nome in lista[c]['nome'] and email in lista[c]['email']:
                print(lista[c])

    elif esc == 3:
        nome = str(input("Digite o nome do usuario: "))
        email = str(input("Digite o email: "))
    
        for c in range(0,len(lista)):
            if  nome in lista[c]['nome'] and email in lista[c]['email']:
                del lista[c]
        
    elif esc == 4:
        with open(path.join(dirpath, "Arquivo.txt"), "w", encoding="utf-8") as arquivo:
           # arquivo.write(f'{"Nomes":<40} {"Emails":>7}\n\n')
            for c in range(0,len(lista)):
                arquivo.write(f'{lista[c]['nome']: <40} > {lista[c]['email']:>7}\n')
                #arquivo.write(f'{lista[c]}\n')
            
    elif esc == 5:
        with open(path.join(dirpath, "Arquivo.txt"), "r") as leitura:
            for linha in leitura:
                nome, email = linha.strip().split(">") 
                lista.append({"nome": nome, "email": email})  

    elif esc == 6:
        print("Encerrando programa!")
        break

    else:
        print("opção invalida!!")
5