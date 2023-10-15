from ecoguard import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    protocolo = database.relationship("Protocolo", backref="usuario", lazy=True)

class Protocolo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tipo = database.Column(database.String, nullable=False)
    local = database.Column(database.String, nullable=False)
    observacao = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)