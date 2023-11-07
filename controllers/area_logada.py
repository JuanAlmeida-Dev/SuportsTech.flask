from flask import render_template, request, session, redirect
from app import app

# Rota da área logada
@app.route('/area_logada')
def area_logada():
    # Verificar se o ID sessão está presente no cookie
    session_id = request.cookies.get("session_id")
    sessoes = session.get("sessoes", {})

    # Redirecionar para a página logada
    if session_id in sessoes:
        email = sessoes[session_id]
        usuario = sessoes[session_id]
        return render_template("area_logada.html", email=email, usuario=usuario)
    else:
        # Em caso de erro redirecionar para a página de login
        return redirect("/login")