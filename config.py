import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234'
    MYSQL_DB = 'graduation_gifts'
    # Caminho absoluto para a pasta de uploads dentro de static
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app', 'static', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}