import unittest
from app import NovoFilme
from app import AtualizarFilme
from app import ExcluirFilme


class TestFilme(unittest.TestCase):
    def test_adicionar_filme(self):
        filme = {"nome": "O Poderoso Chefão", "diretor": "Francis Ford Coppola", "genero": "Drama", "ano": 1972}
        # chamar função de adicionar filme com os parâmetros acima
        # supondo que a função retorna um objeto filme com ID gerado automaticamente
        novo_filme = NovoFilme(filme)
        # verificar se o filme foi adicionado corretamente
        self.assertEqual(novo_filme["nome"], "O Poderoso Chefão")
        self.assertEqual(novo_filme["diretor"], "Francis Ford Coppola")
        self.assertEqual(novo_filme["genero"], "Drama")
        self.assertEqual(novo_filme["ano"], 1972)
        # verificar se o ID foi gerado automaticamente
        self.assertIsNotNone(novo_filme["id"])

    def test_atualizar_filme(self):
        filme = {"nome": "O Poderoso Chefão", "diretor": "Francis Ford Coppola", "genero": "Drama", "ano": 1972}
        # chamar função de atualizar filme com os parâmetros acima
        # supondo que a função retorna um objeto filme atualizado
        filme_atualizado = AtualizarFilme(id, filme)
        # verificar se o filme foi atualizado corretamente
        self.assertEqual(filme_atualizado["nome"], "O Poderoso Chefão")
        self.assertEqual(filme_atualizado["diretor"], "Francis Ford Coppola")
        self.assertEqual(filme_atualizado["genero"], "Ação")
        self.assertEqual(filme_atualizado["ano"], 1999)

    def test_excluir_filme(self):
        id = 1
        # chamar função de excluir filme com o ID do filme existente
        # supondo que a função retorna True se o filme foi excluído com sucesso
        sucesso = ExcluirFilme(id)
        # verificar se o filme foi excluído com sucesso
        self.assertTrue(sucesso)

    def test_adicionar_filme_invalido(self):
        filme = {"nome": "O Senhor dos Anéis", "diretor": "Peter Jackson", "genero": "Fantasia", "ano": 1945}
        # chamar função de adicionar filme com os parâmetros acima
        # supondo que a função retorna None se o filme não for adicionado com sucesso
        filme_adicionado = NovoFilme(filme)
        # verificar se o filme não foi adicionado com sucesso
        self.assertIsNone(filme_adicionado)

    def test_atualizar_filme_inexistente(self):
        filme = {"nome": "Jurassic Park", "diretor": "Steven Spielberg", "genero": "Ação", "ano": 1993}
        # chamar função de atualizar filme com os parâmetros acima e um ID de filme inexistente
        # supondo que a função retorna None se o filme não for atualizado com sucesso
        filme_atualizado = AtualizarFilme(123, filme)
        # verificar se o filme não foi atualizado com sucesso
        self.assertIsNone(filme_atualizado)

    def test_excluir_filme_inexistente(self):
        id_filme_inexistente = 456
        # chamar função de excluir filme com o ID do filme inexistente acima
        # supondo que a função retorna False se o filme não for excluído com sucesso
        sucesso = ExcluirFilme(id_filme_inexistente)
        # verificar se o filme não foi excluído com sucesso
        self.assertFalse(sucesso)