from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model.base import Base


class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(140), unique=True)
    autor = Column(String(140), unique=True)
    genero = Column(String(140), unique=True)

    def __init__(self, titulo:str, autor:str, genero:str):
        """
        Cria um Livro

        Arguments:
            titulo: Titulo da obra.
            autor: Escritor da obra.
            genero: categoria em que o livro se encaixa
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero