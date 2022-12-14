from flask import jsonify, request
from api.despesa import Despesa


def despesa_mes():
    despesas = Despesa()
    if request.method == 'GET':
        despesas = despesas.get_despesas()

        if despesas is not None:
            data = {
                "data": despesas,
                "success": True
            }
            return jsonify(data)
        return {
                "data": [],
                "success": False
            }

    if request.method == 'POST':
        obj = despesas.save_db(request_form=request.form)
        if not obj:
            return {
                "data": [],
                "success": False
            }
        data = {
            "data": obj,
            "success": True
        }
        return jsonify(data)
