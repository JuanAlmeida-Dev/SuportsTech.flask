from flask import  render_template, request, session
from pprint import pprint
from app import app

# Rota do index
@app.route('/')
def index():
    print('dados da sessão', vars(session))
    return render_template('index.html')

# Rota do index
@app.route('/home')
def home():
    print('dados da sessão', vars(session))
    return render_template('index.html')

# Rota que renderiza o formulário de contato
@app.route('/contato')
def contato():
    print('processando requisição GET')
    return render_template('contato.html')

# Rota da tela de confirmação
@app.route('/confirmacao', methods=['POST'])
def confirmacao():
    print('processando requisição POST')
    pprint(request.form)
    name = request.form.get('nome')
    email = request.form.get('email')
    accept_whatsapp = request.form.get('accept-whatsapp')
    print('checkbox whats', accept_whatsapp)

    dados = {
        'name': name,
        'email': email,
        'accept_whatsapp': accept_whatsapp
    }

    return render_template('confirmacao.html', **dados)


