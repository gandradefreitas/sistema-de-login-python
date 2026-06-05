# Sistema de Login

Sistema de login desenvolvido em Python com foco no estudo de programação orientada a objetos, modularização, persistência de dados e segurança de senhas.

## Funcionalidades

* Cadastro de usuários
* Login de usuários
* Listagem de usuários cadastrados
* Validação de nome, e-mail e senha
* Armazenamento de dados em arquivo JSON
* Criptografia de senhas utilizando bcrypt
* Interface textual utilizando Rich

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
└── .gitignore
```

### Arquivos

#### main.py

Ponto de entrada da aplicação.

Responsável por criar a instância do sistema e iniciar sua execução.

#### sistema.py

Contém a classe `SistemaLogin`, responsável pela lógica principal do sistema:

* Cadastro
* Login
* Persistência dos dados
* Verificação de e-mails existentes

#### usuario.py

Contém a classe `Usuario`, utilizada para representar cada usuário cadastrado.

#### interface.py

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
cd Sistema-Login
```

Instale as dependências:

```bash
pip install bcrypt rich
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

Guilherme Freitas

Projeto desenvolvido para fins de estudo e aprendizado em Python.
