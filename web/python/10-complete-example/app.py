import os
from werkzeug.utils import secure_filename
from config import *
from model import *

fundo_atual = "default.jpg"  # Nome de um fundo padrão, precisa ter esse arquivo em static/img

@app.route("/")
def home():
    return render_template("home.html", fundo=fundo_atual)

@app.route("/about")
def about():
    return render_template("about.html", fundo=fundo_atual)

@app.route("/listar_pessoas")
def listar_pessoas():
    with db_session:
        pessoas = Pessoa.select()
        return render_template("listar_pessoas.html", pessoas=pessoas, fundo=fundo_atual)

@app.route("/form_adicionar_pessoa")
def form_adicionar_pessoa():
    return render_template("form_adicionar_pessoa.html", fundo=fundo_atual)

@app.route("/cadastro")
def cadastro():
    try:
        with db_session:
            p = Pessoa(**request.args)
            commit()
        return redirect("/listar_pessoas")
    except Exception as e:
        return f"Houve um erro no nosso sistema super seguro de coleta de dados confidenciais. Erro: {str(e)}"

UPLOAD_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload_fundo", methods=["POST"])
def upload_fundo():
    global fundo_atual
    if 'arquivo' not in request.files:
        return "Ops... parece que você esqueceu de anexar o arquivo."

    arquivo = request.files['arquivo']

    if arquivo.filename == '':
        return "Nome de arquivo vazio.."

    if arquivo:
        nome_seguro = secure_filename(arquivo.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_seguro)
        arquivo.save(caminho)
        fundo_atual = nome_seguro
        return redirect("/")

@app.route("/promocao")
def promocao():
    return render_template("promocao.html", fundo=fundo_atual)


app.run()
