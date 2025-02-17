class Jogador:
    def __init__(self, nome: str, pontos: int):
        self.nome = nome    
        self.pontos = pontos 

    def adicionar_pontos(self, pontos: int) -> int:
        self.pontos += pontos
        return self.pontos

    def __repr__(self) -> str:
        return f"Jogador(nome={self.nome!r}, pontos={self.pontos})"
