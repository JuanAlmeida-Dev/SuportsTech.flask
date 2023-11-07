from flask import redirect, render_template, request, session, make_response
from app import app
import uuid, hashlib 

# Renderiza o formulário de login no GET
@app.route('/login')
def login():
    print('processando requisição GET')
    return render_template('login.html')

# Redireciona para a área logada no POST
@app.route('/login', methods=['POST'])
def login_post():
    # Obtendo valores do formulário de login
    if request.method == "POST":
        email = request.form.get("log_email")
        senha = request.form.get("log_senha")

        usuarios = session.get("usuarios", {})

        mensagem_email = ""
        mensagem_senha = ""

        # Verificando o Email no dicionário de usuários
        if email in usuarios:
            usuario = usuarios[email]
            senha_hash = hashlib.sha256(senha.encode()).hexdigest()

            # Verificando se as senha são iguais 
            if usuario["senha_hash"] == senha_hash:
                # Gerando um ID único para a sessão
                session_id = str(uuid.uuid4())

                # Criando um dicionário de sessões se não existir
                sessoes = session.get("sessoes", {})
                sessoes[session_id] = {"nome": usuario["nome"], "email": email}

                # Atualizar o objeto de sessão com o dicionário de sessões
                session["sessoes"] = sessoes
                print("Sessoes:", sessoes)

                # Configurando o ID único da sessão no cookie da resposta e redireciona para área logada
                response = make_response(redirect("/area_logada"))
                response.set_cookie("session_id", session_id)
                return response
            
            else:
                mensagem_senha = "Senha incorreta!"
        else:
            mensagem_email = "Email não cadastrado!"

        return render_template("login.html",  mensagem_email=mensagem_email, mensagem_senha=mensagem_senha)
    
    return render_template("login.html")

# Rota do logout
@app.route('/logout')
def logout():
    # Remove o ID único da sessão do dicionário de sessões
    session_id = request.cookies.get("session_id")
    sessoes = session.get("sessoes", {})
    if session_id in sessoes:
        del sessoes[session_id]
        session["sessoes"] = sessoes
        print("Sessoes:", sessoes)

    # Remove o cookie do ID de sessão da resposta
    response = make_response(redirect("/login"))
    response.set_cookie("session_id", "", expires=0)

    return response