from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///tareas.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()