.PHONY: help build run test docker-build docker-run clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make build         - (Opcional) Preparar a aplicação (passo customizado, se necessário)"
	@echo "  make run           - Executa a aplicação localmente (usa a interface Flask)"
	@echo "  make test          - Executa a suíte de testes"
	@echo "  make docker-build  - Constrói a imagem Docker da aplicação"
	@echo "  make docker-run    - Roda a aplicação via Docker, mapeando a porta 5000"
	@echo "  make clean         - Remove arquivos temporários e __pycache__"

build:
	@echo "Preparando a aplicação..."
	# Coloque aqui comandos de build se necessário (por exemplo, compilação de assets, etc.)

run:
	@echo "Iniciando a aplicação localmente..."
	python main.py --ui flask

test:
	@echo "Executando os testes..."
	python -m unittest discover -s tests

docker-build:
	@echo "Construindo a imagem Docker..."
	docker build -t my_app_image .

docker-run:
	@echo "Executando a aplicação via Docker..."
	docker run -p 5000:5000 my_app_image

clean:
	@echo "Limpando arquivos temporários..."
	find . -type d -name '__pycache__' -exec rm -rf {} +