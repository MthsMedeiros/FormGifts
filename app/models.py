import os
from app import mysql
from flask import current_app

class Present:
    def __init__(self, id, title, description, image_path, price, link):
        self.id = id
        self.title = title
        self.description = description
        self.image_path = image_path
        self.price = price
        self.link = link

    @staticmethod
    def get_all():
        # Obtém todos os presentes do banco de dados
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM presents")
        presents = cur.fetchall()
        cur.close()
        return presents

    @staticmethod
    def get_by_id(present_id):
        # Obtém um presente pelo seu ID
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM presents WHERE id = %s", (present_id,))
        present = cur.fetchone()
        cur.close()
        return present

    @staticmethod
    def create(title, description, image_filename, price, link):
        # Cria um novo presente
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO presents (title, description, image_path, price, link) VALUES (%s, %s, %s, %s, %s)",
                    (title, description, image_filename, price, link))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def update(present_id, title, description, image_filename, price, link):
        # Atualiza um presente existente
        cur = mysql.connection.cursor()
        cur.execute("UPDATE presents SET title = %s, description = %s, image_path = %s, price = %s, link = %s WHERE id = %s",
                    (title, description, image_filename, price, link, present_id))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete(present_id):
        # Deleta um presente
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM presents WHERE id = %s", (present_id,))
        mysql.connection.commit()
        cur.close()
