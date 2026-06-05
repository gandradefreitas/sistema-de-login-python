"""
Módulo responsável pela interface textual do sistema.

Contém funções de exibição de menus, coleta de dados
do usuário e apresentação de informações na tela.
"""

from rich import print
from getpass import getpass

def menu():
    """
    Exibe o menu principal do sistema e retorna
    a opção escolhida pelo usuário.

    Returns:
        str: Opção informada pelo usuário.
    """

    print('=' * 30)
    print('[green]SISTEMA DE LOGIN[/]')
    print('=' * 30)

    print('[blue][1][/] Cadastrar usuario\n'
          '[blue][2][/] Fazer login\n'
          '[blue][3][/] Listar usuarios\n'
          '[blue][4][/] Sair')
    print()
    return input('Escolha:  ')

def solicitar_login():
    """
    Solicita as credenciais de acesso do usuário.

    Returns:
        tuple[str, str]:
            E-mail e senha informados.
    """

    print('[blue]~[/]' * 40)
    email = input('Informe o seu email: ')

    print('[yellow]A senha ficará oculta durante a digitação.[/]')
    senha = getpass('Informe a senha: ').strip()

    return email, senha

def mostrar_usuarios(registros):
    """
    Exibe todos os usuários cadastrados.

    Args:
        registros (list):
            Lista de objetos Usuario.
    """

    print('=' * 40)
    print('[green]USUÁRIOS CADASTRADOS[/]')
    print('[blue]=[/]' * 40)

    if not registros:
        print('[red]Nenhum usuário cadastrado![/]')
        return

    for usuario in registros:
        print(
            f"[green]Nome[/]: {usuario.nome} | "
            f"[green]Email[/]: {usuario.email}"
        )

    print('[blue]=[/]' * 40)

def solicitar_nome():
    """
    Solicita e valida o nome do usuário.

    O processo se repete até que um nome válido
    seja informado.

    Returns:
        str: Nome validado.
    """

    while True:

        nome = input('Informe o nome: ').strip()

        if not nome:
            exibir_erro('Nome inválido!')
            continue

        if len(nome) > 50:
            exibir_erro('Nome muito longo, maior do que 50 caracteres!')
            continue

        if not nome.replace(' ', '').isalpha():
            exibir_erro('Nome deve conter apenas letras!')
            continue

        return nome

def solicitar_email():
    """
    Solicita e valida um endereço de e-mail.

    O processo se repete até que um e-mail válido
    seja informado.

    Returns:
        str: E-mail validado.
    """

    while True:
        email = input('Informe o email: ').strip().lower()

        if email.count('@') != 1:
            exibir_erro('Email inválido!')
            continue

        parte_local, dominio = email.split('@')

        if parte_local and '.' in dominio:
            return email

        exibir_erro('Email inválido!')

def solicitar_senha():
    """
    Solicita e valida a senha do usuário.

    A senha permanece oculta durante a digitação.

    Returns:
        str: Senha validada.
    """

    while True:

        print('[yellow]A senha ficará oculta durante a digitação.[/]')
        senha = getpass('Informe a senha: ').strip()

        if len(senha) < 8:
            exibir_erro('Senha miníma de 8 caracteres!')
            continue

        if senha.isalpha():
            exibir_erro('A senha deve conter letras e números!')
            continue

        if senha.isdigit():
            exibir_erro('A senha deve conter letras e números!')
            continue

        return senha

def exibir_erro(mensagem):
    """
    Exibe uma mensagem de erro formatada.

    Args:
       mensagem (str):
           Texto do erro a ser exibido.
    """

    print('[purple]=[/]' * 30)
    print(f'[red]{mensagem}[/]')
    print('[purple]=[/]' * 30)