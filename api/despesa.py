import datetime
from data import db


class Despesa:
    def __init__(self):
        self.__valor = None
        self.__data = None
        self.__descricao = None
        self.__tipo_pagamento = None
        self.__categoria = None

    @staticmethod
    def valor(valor):
        try:
            valor = float(valor)
        except Exception as e:
            print(e)
            return False
        return valor

    @staticmethod
    def data(data):
        formato = '%Y-%m-%d'
        if data == '':
            d = datetime.date.today()
            data = d.strftime(formato)
            return data
        else:
            try:
                if datetime.datetime.strptime(data, formato):
                    return data
            except Exception as e:
                print(e)
                return False

    @staticmethod
    def descricao(descricao):
        if type(descricao) != str:
            return False
        return descricao

    @staticmethod
    def tipo_pagamento(tipo_pagamento):
        try:
            tipo_pagamento = int(tipo_pagamento)
        except Exception as e:
            print(e)
            return False

        if tipo_pagamento > 4 or tipo_pagamento < 1:
            return False
        return tipo_pagamento

    @staticmethod
    def categoria(categoria):
        try:
            categoria = int(categoria)
        except Exception as e:
            print(e)
            return False

        if categoria > 4 or categoria < 1:
            return False
        return categoria

    def save_db(self, request_form):
        self.__valor = self.valor(request_form['valor'])
        self.__descricao = self.descricao(request_form['descricao'])
        self.__data = self.data(request_form['data_compra'])
        self.__tipo_pagamento = self.tipo_pagamento(request_form['tipo_pagamento_id'])
        self.__categoria = self.categoria(request_form['categoria_id'])

        if not self.__valor or \
                not self.__data or \
                not self.__descricao or \
                not self.__tipo_pagamento or \
                not self.__categoria:
            return False
        obj = db.post_to_db(valor=self.__valor,
                            data_compra=self.__data,
                            descricao=self.__descricao,
                            tipo_pagamento=self.__tipo_pagamento,
                            categoria=self.__categoria)
        return obj

    def get_despesas(self):
        data = db.get()
        despesas = [
            dict(id=row[0],
                 valor='R${:,.2f}'.format(row[1]),
                 data_compra=row[2],
                 descricao=row[3],
                 tipos_pagamento_id=row[4],
                 categoria_id=row[5]
                 )
            for row in data
        ]
        return despesas
