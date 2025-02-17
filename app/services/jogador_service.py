from app.models.jogador import Jogador

class JogadorService:
    def __init__(self, jogador_dao):
        self.jogador_dao = jogador_dao

    def criar_jogador(self, nome: str, pontos: int) -> Jogador:
        novo_jogador = Jogador(nome, pontos)
        self.jogador_dao.salvar_jogador(novo_jogador)
        return novo_jogador

    def obter_jogador(self, nome: str) -> Jogador:
        return self.jogador_dao.obter_jogador(nome)

    def adicionar_pontos_jogador(self, nome: str, pontos: int) -> int:
        jogador = self.obter_jogador(nome)
        if jogador:
            novo_total = jogador.adicionar_pontos(pontos)
            return novo_total
        else:
            raise ValueError(f"Jogador com nome '{nome}' não encontrado.")
