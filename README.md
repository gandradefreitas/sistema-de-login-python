# Sistema de Login

Sistema de login desenvolvido em Python com foco no estudo de Programação Orientada a Objetos (POO), modularização, persistência de dados e segurança de senhas.

O projeto permite o cadastro e autenticação de usuários utilizando armazenamento local em JSON e criptografia de senhas com bcrypt.

## Funcionalidades

* Cadastro de usuários
* Autenticação de login
* Listagem de usuários cadastrados
* Validação de nome, e-mail e senha
* Armazenamento de dados em arquivo JSON
* Criptografia de senhas utilizando bcrypt
* Interface textual utilizando Rich
* Tratamento de exceções para leitura e gravação de arquivos

## Estrutura do Projeto

```text
Sistema-login-python/
│
├── main.py
├── sistema.py
├── usuario.py
├── interface.py
├── requirements.txt
├── README.md
├── .gitignore
└── usuarios.json (gerado automaticamente)
```

## Descrição dos Arquivos

### main.py

Ponto de entrada da aplicação.

Responsável por criar a instância do sistema e iniciar sua execução.

### sistema.py

Contém a classe `SistemaLogin`, responsável por:

* Cadastro de usuários
* Autenticação de login
* Persistência dos dados
* Verificação de e-mails existentes
* Carregamento e salvamento dos usuários

### usuario.py

Contém a classe `Usuario`, utilizada para representar cada usuário cadastrado.

### interface.py

Responsável pela interação com o usuário:

* Menus
* Entradas de dados
* Exibição de mensagens
* Validações básicas

## Tecnologias Utilizadas

* Python 3
* bcrypt
* Rich
* JSON

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Acesse a pasta do projeto:

```bash
cd Sistema-login-python
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Executar

Execute o arquivo principal:

```bash
python main.py
```

## Exemplo de Uso

```text
[1] Cadastrar usuário
[2] Fazer login
[3] Listar usuários
[4] Sair
```

## Segurança

As senhas dos usuários não são armazenadas em texto puro.

Durante o cadastro, as senhas são criptografadas utilizando bcrypt antes de serem salvas no arquivo JSON.

O arquivo `usuarios.json` é gerado automaticamente durante a execução do sistema e não deve ser versionado no GitHub.

## Conceitos Praticados

Durante o desenvolvimento deste projeto foram praticados:

* Programação Orientada a Objetos (POO)
* Modularização
* Manipulação de arquivos JSON
* Tratamento de exceções
* Hash de senhas com bcrypt
* Validação de entradas
* Organização de projetos Python
* Uso de bibliotecas externas

## Autor

**Guilherme Freitas**

Projeto desenvolvido para fins de estudo e aprendizado em Python.
