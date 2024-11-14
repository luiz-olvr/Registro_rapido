from funcoes import *

Inicio()

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
        AdicionarUser()
        
    elif esc == 1:
        ListaUser()
    
    elif esc == 2:
        PesquisaUser()
    
    elif esc == 3:
        DeletarUser()
    
    elif esc == 4:
        GerarArquivo()
                
    elif esc == 5:
        print("Encerrando programa!")
        break

    else:
        print("opção invalida!!")
