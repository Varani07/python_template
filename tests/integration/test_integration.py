import unittest
from app.dao.jogador_dao import JogadorDAO
from app.services.jogador_service import JogadorService
from tests.cases import TEST_CASES

class TestIntegrationJogador(unittest.TestCase):
    def setUp(self):
        self.dao = JogadorDAO()
        self.service = JogadorService(self.dao)

    def test_criacao_e_obtencao_jogador(self):
        for case in TEST_CASES['jogador']:
            novo_jogador = self.service.criar_jogador(case['nome'], case['pontos'])
            self.assertEqual(novo_jogador.nome, case['nome'])
            self.assertEqual(novo_jogador.pontos, case["pontos"])

            jogador_recuperado = self.service.obter_jogador(case["nome"])
            self.assertIsNotNone(jogador_recuperado)
            self.assertEqual(jogador_recuperado.nome, case["nome"])
            self.assertEqual(jogador_recuperado.pontos, case["pontos"])

if __name__ == "__main__":
    unittest.main()