/**
 * Elemento input responsável por capturar a senha do usuário.
 * O tipo desse input será alternado entre "password" e "text".
 */
const senha = document.getElementById('senha');

/**
 * Elemento de botão/ícone responsável por alternar a visibilidade da senha.
 * Também atualiza os ícones (olho aberto/fechado).
 */
const toggle = document.getElementById('toggleSenha');

/**
 * Evento de clique que alterna a visibilidade da senha.
 *
 * Funcionamento:
 * - Se o input estiver como "password", muda para "text" (mostra a senha)
 * - Se estiver como "text", volta para "password" (oculta a senha)
 *
 * Também atualiza o ícone:
 * - bi-eye → senha oculta
 * - bi-eye-slash → senha visível
 */
toggle.addEventListener('click', () => {

    if (senha.type === 'password') {

        senha.type = 'text';

        toggle.classList.remove('bi-eye');
        toggle.classList.add('bi-eye-slash');

    } else {

        senha.type = 'password';

        toggle.classList.remove('bi-eye-slash');
        toggle.classList.add('bi-eye');

    }

});

/** menssagem de aviso caso o usuário digite o email de forma errada */
const email = document.getElementById("email");
const erroEmail = document.getElementById("erroEmail");

email.addEventListener("input", () => {

    if (email.validity.typeMismatch) {
        erroEmail.textContent = "Digite um email válido (ex: nome@email.com)";
        erroEmail.style.display = "block";
    } else {
        erroEmail.style.display = "none";
    }

});

