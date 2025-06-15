import os
from werkzeug.utils import secure_filename
from config import *
from model import *


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    with db_session:
        # obtém as pessoas
        pessoas = Pessoa.select() 
        return render_template("listar_pessoas.html", pessoas=pessoas)

@app.route("/form_adicionar_pessoa")
def form_adicionar_pessoa():
    return render_template("form_adicionar_pessoa.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    # obter os parâmetros
    nome = request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    # salvar
    with db_session:
        # criar a pessoa
        p = Pessoa(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_pessoas") 

UPLOAD_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload_fundo", methods=["POST"])
def upload_fundo():
    global fundo_atual
    if 'arquivo' not in request.files:
        return "Nenhum arquivo enviado"

    arquivo = request.files['arquivo']

    if arquivo.filename == '':
        return "Nome de arquivo vazio"

    if arquivo:
        nome_seguro = secure_filename(arquivo.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_seguro)
        arquivo.save(caminho)
        fundo_atual = nome_seguro
        return redirect("/")


app.run()

'''
run:
$ flask run
'''
