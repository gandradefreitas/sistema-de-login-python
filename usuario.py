"""
Módulo responsável pela representação de usuários.

Contém a classe Usuario, utilizada para armazenar
os dados de cada usuário cadastrado e realizar a
conversão entre objetos Python e dicionários,
facilitando a persistência dos dados em arquivos JSON.
"""

class Usuario:
    """
    Representa um usuário do sistema.

    Atributos:
        nome (str): Nome do usuário.
        email (str): Endereço de e-mail do usuário.
        senha (str): Senha criptografada do usuário.
    """

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def para_dict(self):
        """
       Converte o objeto Usuario em um dicionário.

       Returns:
           dict: Dicionário contendo nome, email e senha.
        """

        return {
            'Nome': self.nome,
            'Email': self.email,
            'Senha': self.senha
        }

    @classmethod
    def de_dict(cls, dados):
        """
        Cria uma instância de Usuario a partir de um dicionário.

        Args:
            dados (dict): Dicionário contendo os dados do usuário.

        Returns:
            Usuario: Nova instância da classe Usuario.
        """
        
        return cls(
            dados['Nome'],
            dados['Email'],
            dados['Senha']
        )
