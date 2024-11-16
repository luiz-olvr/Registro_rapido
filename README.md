# Registro Rápido  


Este projeto é um **gerenciador de usuários baseado em terminal**, desenvolvido em Python. Ele permite realizar diversas operações com uma lista de usuários, como adicionar, visualizar, pesquisar, deletar e salvar os dados em um arquivo de texto. É uma aplicação simples e prática, ideal para quem deseja aprender sobre manipulação de arquivos, estruturas de dados e interação com o usuário.


---

## 🌟 **Funcionalidades**  
- **Adicionar Usuários:** Cadastre novos usuários com nome e e-mail.  
- **Listar Usuários:** Visualize todos os usuários cadastrados no sistema.  
- **Pesquisar Usuários:** Encontre usuários específicos com base no nome e e-mail.  
- **Excluir Usuários:** Remova usuários diretamente da lista de registros.  
- **Salvar Registros:** Exporte os dados para um arquivo `Registros.txt`.  
- **Carregar Registros:** Continue de onde parou, utilizando dados salvos anteriormente.  

---

## 🛠️ **Pré-requisitos**  
- **Python 3.x** instalado no sistema.  
- Ambiente virtual configurado para isolar as dependências do projeto.  

---

## 📦 **Como baixar e utilizar o executável**  

### **1. Baixando o projeto**  
1. Acesse a página do repositório no GitHub.  
2. Faça o download do repositório clicando em **Code > Download ZIP** ou clone com:  
   ```bash
   git clone https://github.com/seu-usuario/Registro_rapido.git
   ```  

### **2. Utilizando o executável**  
1. Após o download, navegue até a pasta onde o executável está localizado.  
2. Clique duas vezes no executável para iniciar o programa.  
3. Siga as instruções no menu interativo para gerenciar seus registros.

---

<details>
 <summary> 🚀 Como executar o código-fonte  </summary>
## 📦 **Como baixar e configurar o projeto**  

### **1. Baixando o repositório**  
1. Abra o terminal e navegue até a pasta onde deseja salvar o projeto.  
2. Clone o repositório com o comando:  
   ```bash
   git clone https://github.com/seu-usuario/Registro_rapido.git
   ```

### **2. Configurando o ambiente virtual**  
1. Entre no diretório do projeto:  
   ```bash
   cd Registro_rapido
   ```  
2. Crie e ative um ambiente virtual chamado `Registro_rapido`:  
   - **Windows**:  
     ```bash
     python -m venv Registro_rapido  
     Registro_rapido\Scripts\activate
     ```  
   - **Linux/Mac**:  
     ```bash
     python3 -m venv Registro_rapido  
     source Registro_rapido/bin/activate  
     ```  
3. Instale as dependências (caso aplicável):  
   ```bash
   pip install -r requirements.txt
   ```  

📺 Para mais detalhes, confira este excelente tutorial do [Otávio Miranda](https://youtu.be/m1TYpvIYm74?si=0AblG5Alyr2lltaP&t=158) sobre como criar e configurar ambientes virtuais no Python.  

---

## 🚀 **Como executar o programa**  
1. Certifique-se de que o ambiente virtual está ativado.  
2. Execute o script principal:  
   ```bash
   python Registro_rapido.py
   ```  

---
</details>

## 🌱 **Melhorias futuras**  
- Adicionar suporte a banco de dados para maior escalabilidade.  
- Exportar dados em formatos adicionais, como CSV e JSON.  
- Melhorar a interface com suporte a interface gráfica ou web.  
- Implementar testes automatizados para garantir a confiabilidade do código.  

---


#### **Como funciona**
1. O programa inicia carregando os registros existentes de um arquivo (`Registros.txt`) ou começa com uma lista vazia.
2. Um menu interativo é apresentado para o usuário selecionar a operação desejada.
3. As operações são realizadas em memória e podem ser salvas em um arquivo para persistência dos dados.

#### **Destaques técnicos**
- **Manipulação de Arquivos**: Leitura e gravação de dados em um arquivo `.txt`.
- **Estruturas de Dados**: Uso de listas e dicionários para armazenar informações de forma organizada.
- **Interface Simples**: Menu baseado em texto, ideal para iniciantes.
- **Interação com o Sistema**: Uso do `tkinter` para selecionar diretórios e trabalhar com caminhos de arquivos.

#### **Melhorias futuras**
- Implementação de validação mais robusta para entradas do usuário.
- Substituição do formato de texto simples por CSV para maior compatibilidade.
- Melhor formatação de exibição e gravação de dados.
- Adição de testes automatizados para garantir a estabilidade do programa.

---

💻 Desenvolvido com foco em aprendizado e simplicidade!
💻 **Contribuições e sugestões são sempre bem-vindas!**

Caso ache algum erro contate:
  <a href = "mailto:luizrolvr@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
















  
  
  
