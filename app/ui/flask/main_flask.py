from flask import Flask, request, jsonify
from app.dao.jogador_dao import JogadorDAO
from app.services.jogador_service import JogadorService

app = Flask(__name__)

dao = JogadorDAO()
service = JogadorService(dao)

@app.route('/')
def home():
    return "Bem-vindo à API de Jogadores!"

@app.route('/jogador', methods=['POST'])
def criar_jogador():
    data = request.get_json()  
    nome = data.get('nome')
    pontos = data.get('pontos', 0)
    
    jogador = service.criar_jogador(nome, pontos)
    
    return jsonify({"nome": jogador.nome, "pontos": jogador.pontos}), 201

@app.route('/jogador/<nome>', methods=['GET'])
def obter_jogador(nome):
    jogador = service.obter_jogador(nome)
    
    if jogador:
        return jsonify({"nome": jogador.nome, "pontos": jogador.pontos})
    return jsonify({"error": "Jogador não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
