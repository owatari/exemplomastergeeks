from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Contato(Base):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)

    def __str__(self):
        return f"{self.id}, {self.nome}, {self.telefone}, {self.email}"

engine = create_engine('sqlite:///contatos.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()