from flask import Flask
from .routes import api_bp

def create_app():
    # Cria uma instância do aplicativo Flask
    app = Flask(__name__)

    # Configurações do aplicativo
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

    # Registra blueprints, modelos, filtros, etc.
    app.register_blueprint(api_bp, url_prefix='/')

    # Retorna a instância do aplicativo Flask
    return app
