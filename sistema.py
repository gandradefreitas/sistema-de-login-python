"""
Módulo responsável pela lógica principal do sistema de login.

Este módulo contém a classe SistemaLogin, que gerencia:

- Cadastro de usuários;
- Autenticação de login;
- Carregamento e salvamento de dados em arquivo JSON;
- Controle do fluxo principal da aplicação;
- Integração com a interface do usuário.

Os usuários são representados pela classe Usuario e
armazenados em memória durante a execução do programa.
As senhas são protegidas utilizando hash com bcrypt.
"""

import bcrypt
import json
from interface import (
    menu,
    solicitar_nome,
    solicitar_email,
    solicitar_senha,
    solicitar_login,
    mostrar_usuarios,
    exibir_erro
)
from usuario import Usuario
from rich import print

ARQUIVO_USUARIOS = 'usuarios.json'

class SistemaLogin:
    """
   Classe responsável por gerenciar o sistema de login.

   A classe controla o fluxo principal da aplicação,
   incluindo cadastro, autenticação, persistência de
   dados e interação com a interface.

   Attributes:
       registros (list[Usuario]):
           Lista contendo todos os usuários cadastrados.
    """

    def __init__(self):
        self.registros = self.carregar_usuarios()

    def executar(self):
        """
        Executa o menu principal do sistema.

        Permite ao usuário cadastrar-se, realizar login,
        listar usuários cadastrados ou encerrar o programa.
        """

        while True:
            escolha = menu()

            if escolha not in ['1', '2', '3', '4']:
                exibir_erro('[red]Opção inválida![/]')
                continue

            if escolha == '1':
                self.executar_cadastro()

            elif escolha == '2':

                email, senha = solicitar_login()

                usuario = self.login_usuario(email, senha)

                if usuario:
                    print(f'Bem-vindo de volta [yellow]{usuario}[/]!')
                    input('Pressione ENTER para continuar...')
                else:
                    exibir_erro('[red]Email ou senha inválidos![/]')

            elif escolha == '3':
                mostrar_usuarios(self.registros)

                input('Pressione ENTER para voltar...')

            elif escolha == '4':
                break

    def cadastrar_usuario(self, nome, email, senha):
        """
       Cadastra um novo usuário no sistema.

       Args:
           nome (str): Nome do usuário.
           email (str): E-mail do usuário.
           senha (str): Senha em texto puro.

       Returns:
           bool:
               True se o cadastro foi realizado com sucesso.
        """

        senha_hash = bcrypt.hashpw(
            senha.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        usuario = Usuario(
            nome.strip(),
            email.strip().lower(),
            senha_hash
        )
        print('~' * 40)

        self.registros.append(usuario)
        self.salvar_usuarios()
        return True



    def login_usuario(self, email, senha):
        """
        Realiza a autenticação de um usuário.

        Args:
            email (str): E-mail informado.
            senha (str): Senha informada.

        Returns:
            Usuario | None:
                Objeto Usuario autenticado ou None caso
                as credenciais sejam inválidas.
        """
        email = email.strip().lower()

        for usuario in self.registros:

            if email == usuario.email:

                if bcrypt.checkpw(
                        senha.encode('utf-8'),
                        usuario.senha.encode('utf-8')
                ):
                    return {
                        "status": "sucesso",
                        "usuario": usuario
                    }
                else:
                    return {
                        "status": "erro",
                        "tipo": "senha_incorreta"
                    }

        return {
            "status": "erro",
            "tipo": "nao_encontrado"
        }

    def carregar_usuarios(self):
        try:
            with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            usuarios = []

            for usuario in dados:
                usuarios.append(
                    Usuario.de_dict(usuario)
                )

            return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            exibir_erro('[red]Arquivo de usuários corrompido![/]')
            return []

    def salvar_usuarios(self):
        dados = []

        for usuario in self.registros:
            dados.append(usuario.para_dict())

        try:
            with open(ARQUIVO_USUARIOS, 'w') as arquivo:
                json.dump(
                    dados,
                    arquivo,
                    indent=4,
                    ensure_ascii=False
                )

        except OSError:
            exibir_erro('[red]Erro ao salvar usuários[/]!')

    def executar_cadastro(self):

        nome = solicitar_nome()

        while True:

            email = solicitar_email()

            if self.email_existe(email):
                exibir_erro('[red]Email já cadastrado![/]')
                continue

            break

        senha = solicitar_senha()

        if self.cadastrar_usuario(nome, email, senha):
            print('[green]Cadastro realizado com sucesso![/]')

    def email_existe(self, email):

        for usuario in self.registros:
            if usuario.email == email.lower():
                return True

        return False