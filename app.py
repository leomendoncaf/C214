from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import sqlite3

# Cria a conexão com o banco de dados
conn = sqlite3.connect('filmes.db')

# Cria a instância do Flask
app = Flask(__name__)
api = Api(app)

# Classe que representa a API para listar todos os filmes
class Filmes(Resource):
    def get(self):
        # Executa a consulta SQL para listar todos os filmes
        cursor = conn.execute('SELECT * FROM filmes')
        filmes = [{'id': row[0], 'titulo': row[1], 'genero': row[2], 'diretor': row[3], 'ano': row[4]} for row in cursor.fetchall()]

        # Retorna a lista de filmes em formato JSON
        return {'filmes': filmes}

# Classe que representa a API para criar um novo filme
class NovoFilme(Resource):
    def post(self):
        # Define os parâmetros esperados na requisição
        parser = reqparse.RequestParser()
        parser.add_argument('titulo', type=str, required=True)
        parser.add_argument('genero', type=str, required=True)
        parser.add_argument('diretor', type=str, required=True)
        parser.add_argument('ano', type=int, required=True)
        args = parser.parse_args()

        # Insere o novo filme no banco de dados
        conn.execute('INSERT INTO filmes (titulo, genero, diretor, ano) VALUES (?, ?, ?, ?)', (args['titulo'], args['genero'], args['diretor'], args['ano']))
        conn.commit()

        # Retorna uma mensagem de sucesso em formato JSON
        return {'mensagem': 'Filme criado com sucesso'}

# Classe que representa a API para atualizar um filme existente
class AtualizarFilme(Resource):
    def put(self, id):
        # Define os parâmetros esperados na requisição
        parser = reqparse.RequestParser()
        parser.add_argument('titulo', type=str)
        parser.add_argument('genero', type=str)
        parser.add_argument('diretor', type=str)
        parser.add_argument('ano', type=int)
        args = parser.parse_args()

        # Verifica se o filme com o ID informado existe no banco de dados
        cursor = conn.execute('SELECT * FROM filmes WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row is None:
            return {'mensagem': 'Filme não encontrado'}, 404

        # Atualiza os dados do filme no banco de dados
        query = 'UPDATE filmes SET '
        params = []
        if args['titulo'] is not None:
            query += 'titulo = ?, '
            params.append(args['titulo'])
        if args['genero'] is not None:
            query += 'genero = ?, '
            params.append(args['genero'])
        if args['diretor'] is not None:
            query += 'diretor = ?, '
            params.append(args['diretor'])
        if args['ano'] is not None:
            query += 'ano = ?, '
            params.append(args['ano'])
        query = query[:-2] + ' WHERE id = ?'
        params.append(id)
        conn.execute(query, params)
        conn.commit()

        # Retorna uma mensagem de sucesso em formato JSON
        return {'mensagem': 'Filme atualizado com sucesso'}

# Classe que representa a API para excluir um filme existente
class ExcluirFilme(Resource):
    def delete(self, id):
        # Verifica se o filme com o ID informado existe no banco de dados
        cursor = conn.execute('SELECT * FROM filmes WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row is None:
            return {'mensagem': 'Filme não encontrado'}, 404

        # Exclui o filme do banco de dados
        conn.execute('DELETE FROM filmes WHERE id = ?', (id,))
        conn.commit()

        # Retorna uma mensagem de sucesso em formato JSON
        return {'mensagem': 'Filme excluído com sucesso'}

# Adiciona as rotas das APIs à instância do Flask
api.add_resource(Filmes, '/filmes')
api.add_resource(NovoFilme, '/filmes/novo')
api.add_resource(AtualizarFilme, '/filmes/<int:id>')
api.add_resource(ExcluirFilme, '/filmes/<int:id>/excluir')

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)

