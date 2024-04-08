from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = 'flight_table'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    cpf = Column(Integer, nullable=False)
    assento = Column(String(255), nullable=False)
    destino = Column(String(255), nullable=False)
    executivo = Column(Boolean, nullable=False)

engine = create_engine("sqlite:///flight_db.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()