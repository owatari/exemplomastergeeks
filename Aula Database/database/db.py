from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    glasses = Column(Boolean, nullable=False)
    hair = Column(String, nullable=False)
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.age}, {self.height} {self.glasses}, {self.hair}"

engine = create_engine("sqlite:///persondb.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()