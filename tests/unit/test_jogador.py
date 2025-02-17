import unittest
from app.models.jogador import Jogador
from tests.cases import TEST_CASES

class TestJogador(unittest.TestCase):
    def test_cricao_jogador(self):
        for case in TEST_CASES["jogador"]:
            jogador = Jogador(case['nome'], case['pontos'])
            self.assertEqual(jogador.nome, case['nome'])
            self.assertEqual(jogador.pontos, case['pontos'])

    def test_adicionar_pontos(self):
        for case in TEST_CASES["jogador"]:
            jogador = Jogador(case['nome'], case['pontos'])
            jogador.adicionar_pontos(5)
            self.assertEqual(jogador.pontos, case['pontos'] + 5)

if __name__ == "__main__":
    unittest.main()