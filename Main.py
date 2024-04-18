from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import app, redirect, request
from model import Session
from schemas.error import ErrorSchema
from schemas.livro import *
from scriptbd import CriarDB

if __name__ == "__Main__":
    CriarDB()

info = Info(title="API Minha coleção", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
livro_tag = Tag(name="Livro", description="Criação, leitura e exclusão de livros da coleção")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/listalivros', tags=[livro_tag], 
         responses={"200": ListagemLivroSchema, "404": ErrorSchema})
def get_livros():
    """Faz a busca por todos os Livros cadastrados

    Retorna uma representação da coleção de livros.
    """
    session = Session()
    # fazendo a busca
    livros = session.query(Livro).all()

    if not livros:
        # se não há livros cadastrados
        return {"livros": []}, 200
    else:
        # retorna a representação de livros
        print(livros)
        return apresenta_livros(livros), 200

@app.post('/cadastralivro', tags=[livro_tag],
          responses={"200": LivroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_livro():
    """Adiciona um novo Livro à base de dados

    Retorna uma representação dos livros.
    """
    livro_data = request.json

    livro = Livro(
        titulo = livro_data['titulo'],
        autor = livro_data['autor'],
        genero = livro_data['genero']
    )

    session = Session()
    session.add(livro)
    session.commit()

    return apresenta_livro(livro), 200

@app.delete('/apagalivro', tags=[livro_tag],
            responses={"200": LivroDelSchema, "404": ErrorSchema})
def del_livro(query: LivroBuscaSchema):
    """Deleta um Livro a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    livro_id = query.id
    print(livro_id)
    session = Session()
    count = session.query(Livro).filter(Livro.id == livro_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Livro removido", "id": livro_id}
    else:
        # se o livro não foi encontrado
        error_msg = "Livro não encontrado na base :/"
        return {"mesage": error_msg}, 404

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)