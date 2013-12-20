from sqlalchemy.orm import relationship
from app import db


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False, info={'label': 'Server Name'})
    variables = relationship("Variable")

    # def __init__(self, name):
    #     self.name = name


class Variable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(225), nullable=False)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))

    # def __init__(self, name, value, server_id):
    #     self.name = name
    #     self.value = value
    #     self.server_id = server_id