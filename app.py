"""
Aplicação web do sistema de login utilizando Flask.

Este módulo é responsável por:

Configurar e inicializar a aplicação Flask;
Definir as rotas da aplicação;
Receber e processar dados enviados pelos formulários;
Integrar a interface web com a lógica do sistema;
Renderizar as páginas HTML;
Realizar redirecionamentos entre páginas.

Rotas:
/:
Página inicial de cadastro de usuários.

/login:
    Página de autenticação de usuários.

/logout:
    Encerra a sessão atual e retorna para a
    página inicial.

Dependências:
- Flask
- SistemaLogin
- datetime
"""

from flask import Flask, render_template, request, redirect, url_for
from sistema import SistemaLogin
from datetime import datetime

app = Flask(__name__)

sistema = SistemaLogin()

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Exibe a página inicial da aplicação.

    Permite o cadastro de novos usuários através
    de um formulário HTML.

    Returns:
        Response:
            Página de cadastro ou redirecionamento
            para o dashboard após cadastro bem-sucedido.
    """

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        resultado = sistema.cadastrar_usuario(
            nome,
            email,
            senha
        )

        print("Resultado:", resultado)

        return redirect(
            url_for('dashboard')
        )

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Realiza a autenticação de usuários.

    Recebe os dados do formulário de login,
    valida as credenciais e exibe o dashboard
    quando o acesso é autorizado.

    Returns:
        Response:
            Dashboard do usuário autenticado ou
            página de login com mensagem de erro.
    """

    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        if not sistema.email_existe(email):
            return render_template(
                'login.html',
                erro='Usuário não cadastrado.'
            )

        usuario = sistema.login_usuario(
            email,
            senha
        )

        if usuario:
            horario = datetime.now().strftime(
                "%d/%m/%Y às %H:%M"
            )

            return render_template(
                'dashboard.html',
                usuario=usuario,
                horario=horario
            )

        return render_template(
            'login.html',
            erro='Email ou senha inválidos.'
        )

    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Realiza o logout do usuário.

    Redireciona o usuário para a página inicial
    da aplicação.

    Returns:
        Response:
            Redirecionamento para a rota principal.
    """

    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)