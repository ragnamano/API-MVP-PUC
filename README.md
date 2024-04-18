# API-MVP-PUC
Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo aqui é ilutsrar o conteúdo apresentado ao longo das três aulas da disciplina.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 127.0.0.1 --port 5001
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 127.0.0.1 --port 5001 --reload
```

Abra o [http://127.0.0.1:5001/](http://127.0.0.1:5001/) no navegador para verificar o status da API em execução.
