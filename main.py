"""
Arquivo principal da aplicação.

Responsável por criar a instância do sistema
de 'login' e iniciar a execução do programa.

Funções:
    main() -→ Inicializa o sistema e executa
    o menu principal da aplicação.
"""

from sistema import SistemaLogin


def main():
    """
    Cria uma instância do sistema de login
    e inicia a execução da aplicação.
    """

    sistema = SistemaLogin()

    sistema.executar()

if __name__ == '__main__':
    main()