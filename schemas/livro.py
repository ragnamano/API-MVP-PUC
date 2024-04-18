from pydantic import BaseModel
from typing import List
from model.livro import Livro


class LivroSchema(BaseModel):
    """ Define como um novo livro a ser inserido deve ser representado
    """
    titulo: str = "O Código Da Vinci"
    autor: str = "Dan Brown"
    genero: str = "Romance"


class LivroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    id: int


class ListagemLivroSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    livros:List[LivroSchema]


def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for livro in livros:
        result.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "genero": livro.genero,
        })

    return {"livros": result}


class LivroViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    titulo: str 
    autor: str 
    genero: str 


class LivroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    titulo: str

def apresenta_livro(livro: Livro):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "genero": livro.genero,
    }
