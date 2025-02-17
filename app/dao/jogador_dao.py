from app.models.jogador import Jogador

class JogadorDAO:
    def __init__(self):
        self._jogadores = {}

    def salvar_jogador(self, jogador: Jogador) -> Jogador:
        self._jogadores[jogador.nome] = jogador
        return jogador

    def obter_jogador(self, nome: str) -> Jogador:
        return self._jogadores.get(nome)
