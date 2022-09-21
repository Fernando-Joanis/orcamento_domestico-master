import os
from flask import Flask, Blueprint
from api.views.health_views import health
from api.views.despesas_views import despesa_mes


def create_app():
    api = Blueprint('api', __name__)
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.root_path, '../data/database.db')
    )

    # define api routes
    api.add_url_rule('/status', 'health', view_func=health, methods=['GET'])
    api.add_url_rule('/despesas', 'despesas', view_func=despesa_mes, methods=['GET', 'POST'])

    app.register_blueprint(api, url_prefix='/api')
    return app
