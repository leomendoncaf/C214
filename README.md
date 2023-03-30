# CRUD básico de filmes com APIs
Este projeto é um CRUD básico de filmes implementado em Python utilizando o framework Flask e a extensão Flask-RESTful. As APIs REST criadas permitem listar, criar, atualizar e excluir filmes do banco de dados.

## Instalação
Para executar o projeto, siga os passos abaixo:

1. Clone o repositório para sua máquina:

```git clone https://github.com/leomendoncaf/C214```

2. Instale as dependências necessárias:

```pip install -r requirements.txt```

3. Inicie o servidor Flask:

```python app.py```

## Uso

As APIs criadas permitem realizar as seguintes operações em relação aos filmes:

Listar todos os filmes: GET /filmes

Criar um novo filme: POST /filmes/novo

Atualizar um filme existente: PUT /filmes/<id>

Excluir um filme existente: DELETE /filmes/<id>/excluir

`As requisições devem ser enviadas no formato JSON, com os seguintes parâmetros:`

-titulo (string): título do filme;

-genero (string): gênero do filme;

-diretor (string): nome do diretor do filme;

-ano (integer): ano de lançamento do filme.

## Exemplo de requisição

Para criar um novo filme, envie uma requisição POST para o endpoint /filmes/novo com os parâmetros do filme a ser criado no corpo da requisição:
```
POST http://localhost:5000/filmes/novo
Content-Type: application/json

{
    "titulo": "O Poderoso Chefão",
    "genero": "Drama",
    "diretor": "Francis Ford Coppola",
    "ano": 1972
}
```

## Exemplo de resposta

A resposta da requisição será um objeto JSON com a mensagem de sucesso ou de erro, dependendo do resultado da operação:
```
{
    "mensagem": "Filme criado com sucesso"
}
```
