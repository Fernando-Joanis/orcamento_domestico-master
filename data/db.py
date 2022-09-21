import sqlite3
from flask import current_app, g
import datetime

db = None
cursor = None


def connect_db():
    global db, cursor
    if db is None:
        db = sqlite3.connect(current_app.config['DATABASE'],
                             detect_types=sqlite3.PARSE_DECLTYPES,
                             check_same_thread=False)
        cursor = db.cursor()

    return db, cursor


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get():
    connect_db()
    month = datetime.date.today().month
    year = datetime.date.today().year
    data = cursor.execute('SELECT d.id, d.valor, d.data_compra, d.descricao, tipo.tipo AS tipo_pagamento,'
                          ' cat.nome AS categoria '
                          'FROM despesas AS d '
                          'INNER JOIN tipos_pagamento AS tipo ON d.tipo_pagamento_id = tipo.id '
                          'INNER JOIN categorias AS cat ON d.categoria_id = cat.id '
                          f'WHERE d.data_compra > "{year}-{month:0>2d}-01" '
                          f'AND d.data_compra < "{year}-{month:0>2d}-31"').fetchall()
    return data


def post_to_db(valor, data_compra, descricao, tipo_pagamento, categoria):
    connect_db()
    sql = """ INSERT INTO despesas (valor, data_compra, descricao, tipo_pagamento_id, categoria_id)
                      VALUES (?, ?, ?, ? ,?)"""
    cursor.execute(sql, (valor, data_compra, descricao, tipo_pagamento, categoria))
    db.commit()
    return cursor.lastrowid
