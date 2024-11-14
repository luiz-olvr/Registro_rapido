from os import path
from tkinter import filedialog

lista = list()


def Inicio():
    criar = int(input("Deseja criar novos arquivos[ 0 ]?\nContinuar com os antigos[ 1 ]?\nEscolha: "))
    if criar == 1:
        dirpath = filedialog.askdirectory()
        with open(path.join(dirpath, "Arquivo.txt"), "r") as leitura:
            for linha in leitura:
                nome, email = linha.strip().split(">") 
                lista.append({"nome": nome, "email": email})  


def AdicionarUser():
    while nome  or email != "0":
        print("Digite 0 Para sair!!!")  
        nome = str(input("Digite o nome do usuario: "))
        email = str(input("Digite o email: "))
        if nome or email == "0":
            break
        for c in range(0,len(lista)):
            if  nome in lista[c]['nome'] and email in lista[c]['email']:
                print("Usuario já existente!")
        lista.append({"nome": nome, "email": email})

def ListaUser():
     for c in range(0,len(lista)):
        print(f'\nUsuario : {lista[c]['nome']} \nEmail: {lista[c]['email']}\n')
            
            
            
def PesquisaUser():
    nome = str(input("Digite o nome do usuario: "))
    email = str(input("Digite o email: "))
    for c in range(0,len(lista)):
        if  nome in lista[c]['nome'] and email in lista[c]['email']:
            print(lista[c])



def DeletarUser():
    nome = str(input("Digite o nome do usuario: "))
    email = str(input("Digite o email: "))
    for c in range(0,len(lista)):
        if  nome in lista[c]['nome'] and email in lista[c]['email']:
            del lista[c]



def GerarArquivo():
    dirpath = filedialog.askdirectory()
    with open(path.join(dirpath, "Arquivo.txt"), "w", encoding="utf-8") as arquivo:
            for c in range(0,len(lista)):
                arquivo.write(f'{lista[c]['nome']: <40} > {lista[c]['email']:>7}\n')
            
