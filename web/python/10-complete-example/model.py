from config import *
from datetime import date
from decimal import Decimal

class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)  # Chave primária automática
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    cpf = Required(str)
    rg = Required(str)
    nascimento = Required(date)
    cep = Required(str)
    nome_mae = Required(str)
    digitos_cartao = Required(int)
    saldo = Required(Decimal)  # Tipo decimal pra valores de dinheiro

    def __init__(self):
        pass
    
    def __str__(self):
        return f'{self.nome}, {self.email}, {self.telefone}'

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)
