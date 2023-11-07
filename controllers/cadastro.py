from flask import render_template, request, session, redirect
import hashlib
from app import app

# Renderiza o formulário de cadastro no GET
@app.route('/cadastro')
def cadastro():
    print('processando requisição GET')
    return render_template('cadastro.html')

# Redireciona para o /Login no POST
@app.route("/cadastro", methods=["POST"])
def cadastro_post():
    print("processando requisição POST")
    # Obtendo valores do formulário de cadastro
    if request.method == "POST":
        nome = request.form.get("cad_nome")
        email = request.form.get("cad_email")
        senha = request.form.get("cad_senha")
        confirma_senha = request.form.get("confirma_senha")

        # Dicionário de sessão
        usuarios = session.get("usuarios", {})

        mensagem_email = ""
        mensagem_senha = ""

        # Verificando se a senha está correta
        if senha != confirma_senha:
            mensagem_senha = "Senha incorreta!"
        # Verificando se o Email já foi cadastrado
        elif email in usuarios:
            mensagem_email = "Email já cadastrado!"
        else:
            # Gerar o hash da senha
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()

            # Adicionar o usuário ao dicionário de usuários
            novo_usuario = {"nome": nome, "email": email, "senha_hash": senha_hash}
            usuarios[email] = novo_usuario
            session["usuarios"] = usuarios
            print("Usuário cadastrado:", novo_usuario)
            print("Usuários:", usuarios)

            # Redireciona para o /Login
            return redirect("/login")
        
    return render_template("cadastro.html", mensagem_senha=mensagem_senha, mensagem_email=mensagem_email)
    

