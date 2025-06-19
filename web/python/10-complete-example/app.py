
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect
from pony.orm import *
from model import *
from datetime import datetime
from decimal import Decimal

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

fundo_atual = "default.jpg"

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

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html", fundo=fundo_atual)

@app.route("/cadastrar")
def cadastrar():
    try:
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

        if not nascimento:
            return "Data de nascimento não foi preenchida."
        try:
            nascimento_convertido = datetime.strptime(nascimento, '%Y-%m-%d').date()
        except ValueError:
            return "Formato de data inválido. Use o formato YYYY-MM-DD."

        digitos_cartao_int = int(digitos_cartao)
        saldo_decimal = Decimal(saldo)

        with db_session:
            Pessoa(
                nome=nome,
                email=email,
                telefone=telefone,
                cpf=cpf,
                rg=rg,
                nascimento=nascimento_convertido,
                cep=cep,
                nome_mae=nome_mae,
                digitos_cartao=digitos_cartao_int,
                saldo=saldo_decimal
            )

        return redirect("/listar_pessoas")
    except Exception as e:
        return f"Erro ao cadastrar: {str(e)}"

@app.route("/upload_fundo", methods=["POST"])
def upload_fundo():
    global fundo_atual
    if 'arquivo' not in request.files:
        return "Ops... você esqueceu de anexar o arquivo."
    arquivo = request.files['arquivo']
    if arquivo.filename == '':
        return "Nome de arquivo vazio."
    if arquivo:
        nome_seguro = secure_filename(arquivo.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_seguro)
        caminho_absoluto = os.path.join(os.path.abspath(os.path.dirname(__file__)), caminho)
        try:
            arquivo.save(caminho_absoluto)
            fundo_atual = nome_seguro
            return redirect("/")
        except Exception as e:
            return f"Erro ao salvar o arquivo: {str(e)}"

@app.route("/promocao")
def promocao():
    return render_template("promocao.html", fundo=fundo_atual)

app.run(debug=True)
