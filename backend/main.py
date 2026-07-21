from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defina caminhos absolutos para a pasta de imagens usando PASTA_BASE e PASTA_IMAGENS
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista chamada figurinhas com as 50 figurinhas do álbum.
# As figurinhas de 6 a 50 estão comentadas pois ainda não têm imagens correspondentes na pasta.
figurinhas = [
    {"id": 1, "nome": "Homem de Ferro", "categoria": "super-heroi", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Batman", "categoria": "super-heroi", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Homem Aranha", "categoria": "super-heroi", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Mulher Maravilha", "categoria": "super-heroi", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Super Homem", "categoria": "super-heroi", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Harry Potter", "categoria": "fantasia-rpg", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Gandalf", "categoria": "fantasia-rpg", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Geralt de Rívia", "categoria": "fantasia-rpg", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Frodo Bolseiro", "categoria": "fantasia-rpg", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Hermione Granger", "categoria": "fantasia-rpg", "imagem_url": "/figurinhas/10/imagem"},
    # Figurinhas que ainda não estão disponíveis (imagens ausentes na pasta):
    
    # {"id": 11, "nome": "Luke Skywalker", "categoria": "ficcao-cientifica", "imagem_url": "/figurinhas/11/imagem"},
    # {"id": 12, "nome": "Spock", "categoria": "ficcao-cientifica", "imagem_url": "/figurinhas/12/imagem"},
    # {"id": 13, "nome": "Darth Vader", "categoria": "ficcao-cientifica", "imagem_url": "/figurinhas/13/imagem"},
    # {"id": 14, "nome": "Neo", "categoria": "ficcao-cientifica", "imagem_url": "/figurinhas/14/imagem"},
    # {"id": 15, "nome": "Ellen Ripley", "categoria": "ficcao-cientifica", "imagem_url": "/figurinhas/15/imagem"},
    # {"id": 16, "nome": "Goku", "categoria": "anime-classicos", "imagem_url": "/figurinhas/16/imagem"},
    # {"id": 17, "nome": "Seiya de Pégaso", "categoria": "anime-classicos", "imagem_url": "/figurinhas/17/imagem"},
    # {"id": 18, "nome": "Naruto Uzumaki", "categoria": "anime-classicos", "imagem_url": "/figurinhas/18/imagem"},
    # {"id": 19, "nome": "Ichigo Kurosaki", "categoria": "anime-classicos", "imagem_url": "/figurinhas/19/imagem"},
    # {"id": 20, "nome": "Monkey D. Luffy", "categoria": "anime-classicos", "imagem_url": "/figurinhas/20/imagem"},
    # {"id": 21, "nome": "Rudo Surebrec", "categoria": "anime-novagerecao", "imagem_url": "/figurinhas/21/imagem"},
    # {"id": 22, "nome": "Frieren", "categoria": "anime-novagerecao", "imagem_url": "/figurinhas/22/imagem"},
    # {"id": 23, "nome": "Tanjiro Kamado", "categoria": "anime-novagerecao", "imagem_url": "/figurinhas/23/imagem"},
    # {"id": 24, "nome": "Satoru Gojo", "categoria": "anime-novagerecao", "imagem_url": "/figurinhas/24/imagem"},
    # {"id": 25, "nome": "Sung Jin-Woo", "categoria": "anime-novagerecao", "imagem_url": "/figurinhas/25/imagem"},
    # {"id": 26, "nome": "Cloud Strife", "categoria": "jogos-games", "imagem_url": "/figurinhas/26/imagem"},
    # {"id": 27, "nome": "Kratos", "categoria": "jogos-games", "imagem_url": "/figurinhas/27/imagem"},
    # {"id": 28, "nome": "Ahri", "categoria": "jogos-games", "imagem_url": "/figurinhas/28/imagem"},
    # {"id": 29, "nome": "Paladino Danse", "categoria": "jogos-games", "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "Master Chief", "categoria": "jogos-games", "imagem_url": "/figurinhas/30/imagem"},
    # {"id": 31, "nome": "Guilherme Briggs", "categoria": "celebridades", "imagem_url": "/figurinhas/31/imagem"},
    # {"id": 32, "nome": "Wendel Bezerra", "categoria": "celebridades", "imagem_url": "/figurinhas/32/imagem"},
    # {"id": 33, "nome": "Hideo Kojima", "categoria": "celebridades", "imagem_url": "/figurinhas/33/imagem"},
    # {"id": 34, "nome": "Robert Downey Jr.", "categoria": "celebridades", "imagem_url": "/figurinhas/34/imagem"},
    # {"id": 35, "nome": "Chadwick Boseman", "categoria": "celebridades", "imagem_url": "/figurinhas/35/imagem"},
    # {"id": 36, "nome": "Hiroyuki Sawano", "categoria": "musica-trilhas", "imagem_url": "/figurinhas/36/imagem"},
    # {"id": 37, "nome": "LiSA", "categoria": "musica-trilhas", "imagem_url": "/figurinhas/37/imagem"},
    # {"id": 38, "nome": "7 Minutoz", "categoria": "musica-trilhas", "imagem_url": "/figurinhas/38/imagem"},
    # {"id": 39, "nome": "Enygma", "categoria": "musica-trilhas", "imagem_url": "/figurinhas/39/imagem"},
    # {"id": 40, "nome": "Victor Borba", "categoria": "musica-trilhas", "imagem_url": "/figurinhas/40/imagem"},
    # {"id": 41, "nome": "Sabre de Luz", "categoria": "gadgets-memes", "imagem_url": "/figurinhas/41/imagem"},
    # {"id": 42, "nome": "Um Anel", "categoria": "gadgets-memes", "imagem_url": "/figurinhas/42/imagem"},
    # {"id": 43, "nome": "É mais de 8000!", "categoria": "gadgets-memes", "imagem_url": "/figurinhas/43/imagem"},
    # {"id": 44, "nome": "DeLorean DMC-12", "categoria": "gadgets-memes", "imagem_url": "/figurinhas/44/imagem"},
    # {"id": 45, "nome": "Não tenho interesse", "categoria": "gadgets-memes", "imagem_url": "/figurinhas/45/imagem"},
    # {"id": 46, "nome": "Zangado", "categoria": "criadores-comunidade", "imagem_url": "/figurinhas/46/imagem"},
    # {"id": 47, "nome": "EiNerd / Peter Jordan", "categoria": "criadores-comunidade", "imagem_url": "/figurinhas/47/imagem"},
    # {"id": 48, "nome": "Ricardo Cruz", "categoria": "criadores-comunidade", "imagem_url": "/figurinhas/48/imagem"},
    # {"id": 49, "nome": "BRKsEDU", "categoria": "criadores-comunidade", "imagem_url": "/figurinhas/49/imagem"},
    # {"id": 50, "nome": "Imaginago", "categoria": "criadores-comunidade", "imagem_url": "/figurinhas/50/imagem"},
]

# Crie o endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas ativas
    return figurinhas

# Crie o endpoint GET "/figurinhas/{id}/imagem" que busca e retorna a imagem correspondente usando glob
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Retorna 404 se não encontrar nenhuma imagem
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada para esta figurinha.")
    
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(arquivos[0])
