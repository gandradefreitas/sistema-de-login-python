"""
Arquivo principal da aplicação.

Responsável por criar uma instância do sistema
de login e iniciar a execução do programa.

Funções:

main(): Inicializa o sistema e executa o fluxo
principal da aplicação.
"""

from sistema import SistemaLogin

def main():
    """
    Inicializa o sistema de login e inicia
    a execução da aplicação.

    Cria uma instância da classe SistemaLogin
    e executa o menu principal do sistema.
    """

    sistema = SistemaLogin()

    sistema.executar()

if __name__ == '__main__':
    main()