
from pony.orm import *
from datetime import date
from decimal import Decimal

db = Database()

class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)
    cpf = Required(str)
    rg = Required(str)
    nascimento = Required(date)
    cep = Required(str)
    nome_mae = Required(str)
    digitos_cartao = Required(int)
    saldo = Required(Decimal)

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)
