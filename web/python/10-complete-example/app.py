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

@app.route("/cadastrar")
def cadastrar():
    nome = request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    cpf = request.args.get("cpf")
    rg = request.args.get("rg")
    nascimento = request.args.get("nascimento")
    cep = request.args.get("cep")
    nome_mae = request.args.get("nome_mae")
    digitos_cartao = request.args.get("digitos_cartao")
    saldo = request.args.get("saldo")
    
    return redirect("listar_pessoas")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

UPLOAD_FOLDER = os.path.join('static', 'images')
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
        caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), UPLOAD_FOLDER, nome_seguro)
        arquivo.save(caminho)
        
        return arquivo.filename
        fundo_atual = arquivo.filename
        
        return redirect("/")

@app.route("/promocao")
def promocao():
    return render_template("promocao.html")


app.run()
