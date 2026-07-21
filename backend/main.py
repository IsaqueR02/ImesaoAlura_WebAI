# Importa as classes necessárias do FastAPI, StaticFiles e a biblioteca os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

# 1. Cria a instância da aplicação FastAPI
app = FastAPI()

# Configuração do CORS para permitir que o frontend acesse o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Defina o caminho absoluto da pasta de imagens (para o servidor encontrar a pasta independente de onde for executado)
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Configure os arquivos estáticos: "monte" a pasta PASTA_IMAGENS na rota "/imgs" usando StaticFiles, com name="imgs"
# Assim, "figurinhas/01-iron_man.jpg" fica acessível em "/imgs/01-iron_man.jpg"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# 4. Lista contendo as figurinhas cadastradas
figurinhas = [
    {"id": 1, "nome": "Homem de Ferro", "categoria": "super-heroi", "imagem_url": "/imgs/iron_man.jpg"},
    {"id": 2, "nome": "Batman", "categoria": "super-heroi", "imagem_url": "/imgs/batman.jpg"},
    {"id": 3, "nome": "Homem Aranha", "categoria": "super-heroi", "imagem_url": "/imgs/spider_man.jpg"},
    {"id": 4, "nome": "Mulher Maravilha", "categoria": "super-heroi", "imagem_url": "/imgs/wonder_woman.jpg"},
    {"id": 5, "nome": "Super Homem", "categoria": "super-heroi", "imagem_url": "/imgs/superman.jpg"},    
    
    
]

# 5. Endpoint GET "/figurinhas" (função listar_figurinhas) que retorna a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de dicionários que será convertida em JSON automaticamente
    return figurinhas
