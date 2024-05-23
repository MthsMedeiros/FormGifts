from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from .models import Present
import os

main = Blueprint('main', __name__)

def allowed_file(filename):
    # Verifica se o arquivo tem uma extensão permitida
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@main.route('/')
def index():
    # Renderiza a página principal com todos os presentes para os convidados
    presents = Present.get_all()
    return render_template('guest.html', presents=presents)

@main.route('/admin')
def admin():
    # Renderiza a página de administração com todos os presentes para o administrador
    presents = Present.get_all()
    return render_template('admin.html', presents=presents)

@main.route('/admin/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Processa o formulário de criação de um novo presente
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        link = request.form['link']
        image = request.files['image']

        if image and allowed_file(image.filename):
            # Salva a imagem se for um arquivo válido
            filename = secure_filename(image.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            Present.create(title, description, filename, price, link)
            return redirect(url_for('main.admin'))
        else:
            flash('Arquivo de imagem inválido')

    return render_template('edit.html', action="Create")

@main.route('/admin/edit/<int:present_id>', methods=['GET', 'POST'])
def edit(present_id):
    present = Present.get_by_id(present_id)
    if request.method == 'POST':
        # Processa o formulário de edição de um presente existente
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        link = request.form['link']
        image = request.files['image']

        if image and allowed_file(image.filename):
            # Salva a nova imagem se for um arquivo válido
            filename = secure_filename(image.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            Present.update(present_id, title, description, filename, price, link)
        else:
            # Mantém a imagem existente se nenhum novo arquivo foi carregado
            Present.update(present_id, title, description, present[3], price, link)

        return redirect(url_for('main.admin'))

    return render_template('edit.html', present=present, action="Edit")

@main.route('/admin/delete/<int:present_id>', methods=['POST'])
def delete(present_id):
    # Deleta um presente
    Present.delete(present_id)
    return redirect(url_for('main.admin'))
