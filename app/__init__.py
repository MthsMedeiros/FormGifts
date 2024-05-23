from flask import Flask
from flask_mysqldb import MySQL
from config import Config
import os

# Instância do MySQL
mysql = MySQL()


def create_app():
    # Cria uma instância da aplicação Flask
    app = Flask(__name__)

    # Carrega as configurações da aplicação
    app.config.from_object(Config)

    # Inicializa a extensão MySQL com a aplicação Flask
    mysql.init_app(app)

    # Cria a pasta de uploads se não existir
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Importa e registra o blueprint das rotas
    from .routes import main
    app.register_blueprint(main)

    return app
