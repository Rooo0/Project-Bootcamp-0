import db
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import db
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(db.Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(60))
    apellidos = Column(String(255))
    email = Column(String(60))

    def __init__ (self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        

    def __repr__(self):
        return f'{self.id}, {self.nombre}, {self.apellidos}, {self.email}'


class Tarea(db.Base):
    __tablename__ = 'tarea'

    id = Column(Integer, primary_key = True)
    titulo = Column(String(60))
    descripcion = Column(String(255))
    estado = Column(String(60))
    fecha_creacion = Column(String(60))

    responsable = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref = "tarea")

    def __init__ (self, titulo, descripcion, estado, responsable, fecha_creacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.responsable = responsable
        self.fecha_creacion = fecha_creacion
    
    def __repr__(self):
        return f'{self.id}, {self.titulo}, {self.descripcion}, {self.estado}, {self.responsable}, {self.fecha_creacion}'

class Estado(db.Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(60))
    descripcion = Column(String(255))

    def __init__ (self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f'{self.id}, {self.nombre}, {self.descripcion}'


db.Base.metadata.create_all(db.engine)