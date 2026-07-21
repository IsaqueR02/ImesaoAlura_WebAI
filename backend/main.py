# Importa as classes necessárias do FastAPI e Pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Cria a instância da aplicação FastAPI
app = FastAPI()

# --- MODELOS PYDANTIC PARA VALIDAÇÃO DOS DADOS ---

# Modelo para representar uma Figurinha
class Figurinha(BaseModel):
    numero: str
    nome: str
    descricao: str

# Modelo para representar uma Seção
class Secao(BaseModel):
    id: int
    titulo: str
    descricao: str

# --- DADOS DE EXEMPLO (ESTÁTICOS) ---

# Lista contendo as 10 seções do álbum do tema Geek/Nerd
SECOES_MOCK = [
    Secao(id=1, titulo="Super-heróis", descricao="Figurinhas de heróis e heroínas dos quadrinhos."),
    Secao(id=2, titulo="Fantasia & RPG", descricao="Elementos lendários, magos e aventuras de tabuleiro."),
    Secao(id=3, titulo="Ficção Científica", descricao="Naves, inteligências artificiais e viagens espaciais/temporais."),
    Secao(id=4, titulo="Anime & Mangá - Clássicos", descricao="Personagens eternos que marcaram gerações."),
    Secao(id=5, titulo="Anime & Mangá - Nova Geração", descricao="Novos sucessos e fenômenos globais da cultura pop japonesa."),
    Secao(id=6, titulo="Jogos & Games", descricao="Ícones dos consoles e computadores."),
    Secao(id=7, titulo="Celebridades (Atores & Dubladores)", descricao="Personalidades marcantes das telas e das vozes no Brasil."),
    Secao(id=8, titulo="Música & Trilhas", descricao="Compositores e artistas que criaram trilhas sonoras lendárias."),
    Secao(id=9, titulo="Gadgets, Símbolos & Memes", descricao="Tecnologia, nostalgia e a zoeira sem fim da internet."),
    Secao(id=10, titulo="Criadores & Comunidade", descricao="Pioneiros da computação e a comunidade que move a tecnologia.")
]

# Dicionário mapeando o ID de cada seção para a lista de suas respectivas figurinhas (50 figurinhas no total)
FIGURINHAS_MOCK = {
    1: [
        {"numero": "#01", "nome": "Homem de Ferro", "descricao": "O bilionário Tony Stark em sua armadura de alta tecnologia."},
        {"numero": "#02", "nome": "Batman", "descricao": "O cavaleiro das trevas protetor de Gotham City."},
        {"numero": "#03", "nome": "Homem-Aranha", "descricao": "O amigão da vizinhança Peter Parker."},
        {"numero": "#04", "nome": "Mulher-Maravilha", "descricao": "A lendária princesa guerreira amazona de Themyscira."},
        {"numero": "#05", "nome": "Super-Homem", "descricao": "O último filho de Krypton e maior protetor da Terra."}
    ],
    2: [
        {"numero": "#06", "nome": "Gandalf o Cinzento", "descricao": "O sábio e poderoso mago do universo de O Senhor dos Anéis."},
        {"numero": "#07", "nome": "D20", "descricao": "O clássico dado de 20 faces essencial para rolagens de RPG."},
        {"numero": "#08", "nome": "Geralt de Rívia", "descricao": "O lendário bruxo mutante caçador de monstros."},
        {"numero": "#09", "nome": "Mestre dos Magos", "descricao": "O enigmático guia dos jovens no clássico Caverna do Dragão."},
        {"numero": "#10", "nome": "Espada de Longclaw", "descricao": "A famosa espada de aço valiriano empunhada por Jon Snow."}
    ],
    3: [
        {"numero": "#11", "nome": "Darth Vader", "descricao": "O temido lorde sith de Star Wars comandando a Estrela da Morte."},
        {"numero": "#12", "nome": "DeLorean DMC-12", "descricao": "A icônica máquina do tempo sobre rodas de De Volta Para o Futuro."},
        {"numero": "#13", "nome": "Spock", "descricao": "O lógico oficial de ciências vulcano da USS Enterprise em Star Trek."},
        {"numero": "#14", "nome": "Neo", "descricao": "O escolhido que consegue manipular a realidade simulada da Matrix."},
        {"numero": "#15", "nome": "HAL 9000", "descricao": "A inteligência artificial supercomputadora de 2001: Uma Odisseia no Espaço."}
    ],
    4: [
        {"numero": "#16", "nome": "Goku", "descricao": "O lendário guerreiro saiyajin defensor da Terra em Dragon Ball Z."},
        {"numero": "#17", "nome": "Seiya de Pégaso", "descricao": "O obstinado cavaleiro de bronze defensor de Atena."},
        {"numero": "#18", "nome": "Naruto Uzumaki", "descricao": "O jovem ninja que busca se tornar Hokage da Aldeia da Folha."},
        {"numero": "#19", "nome": "Luffy", "descricao": "O carismático capitão dos Chapéus de Palha em busca do One Piece."},
        {"numero": "#20", "nome": "Sailor Moon", "descricao": "A guerreira mágica do amor e da justiça da Lua."}
    ],
    5: [
        {"numero": "#21", "nome": "Tanjirou Kamado", "descricao": "O caçador de demônios determinado de Demon Slayer."},
        {"numero": "#22", "nome": "Deku (Izuku Midoriya)", "descricao": "O jovem herói herdeiro do One For All em My Hero Academia."},
        {"numero": "#23", "nome": "Gojo Satoru", "descricao": "O carismático e imbatível feiticeiro jujutsu de Jujutsu Kaisen."},
        {"numero": "#24", "nome": "Eren Yeager", "descricao": "O jovem que busca a liberdade além das muralhas em Attack on Titan."},
        {"numero": "#25", "nome": "Anya Forger", "descricao": "A adorável garotinha telepata que ama amendoins de Spy x Family."}
    ],
    6: [
        {"numero": "#26", "nome": "Mario", "descricao": "O herói encanador mais famoso e querido do mundo dos videogames."},
        {"numero": "#27", "nome": "Link", "descricao": "O guerreiro escolhido para salvar a princesa Zelda e o reino de Hyrule."},
        {"numero": "#28", "nome": "Pikachu", "descricao": "O simpático monstrinho elétrico símbolo da franquia Pokémon."},
        {"numero": "#29", "nome": "Steve", "descricao": "O clássico protagonista padrão do mundo de blocos de Minecraft."},
        {"numero": "#30", "nome": "Kratos", "descricao": "O implacável Fantasma de Esparta e Deus da Guerra."}
    ],
    7: [
        {"numero": "#31", "nome": "Keanu Reeves", "descricao": "O querido e carismático actor de Matrix, John Wick e lenda da internet."},
        {"numero": "#32", "nome": "Stan Lee", "descricao": "O lendário criador do universo Marvel e mestre das participações especiais."},
        {"numero": "#33", "nome": "Guilherme Briggs", "descricao": "Um dos dubladores brasileiros mais icônicos, conhecido por dublar o Superman e Buzz Lightyear."},
        {"numero": "#34", "nome": "Wendel Bezerra", "descricao": "Renomado dublador brasileiro, a voz eterna de Goku e Bob Esponja."},
        {"numero": "#35", "nome": "Pedro Pascal", "descricao": "O aclamado ator que brilha em The Mandalorian e The Last of Us."}
    ],
    8: [
        {"numero": "#36", "nome": "John Williams", "descricao": "O gênio responsável pelas trilhas de Star Wars, Harry Potter e Indiana Jones."},
        {"numero": "#37", "nome": "Daft Punk", "descricao": "A lendária dupla de música eletrônica com icônicos capacetes futuristas."},
        {"numero": "#38", "nome": "Nobuo Uematsu", "descricao": "O mestre compositor das inesquecíveis trilhas de Final Fantasy."},
        {"numero": "#39", "nome": "Koji Kondo", "descricao": "Compositor das melodias atemporais de Super Mario e The Legend of Zelda."},
        {"numero": "#40", "nome": "Hans Zimmer", "descricao": "Aclamado compositor de trilhas épicas como Interestelar, A Origem e O Rei Leão."}
    ],
    9: [
        {"numero": "#41", "nome": "Raspberry Pi", "descricao": "O mini computador de placa única favorito dos hobbistas e makers."},
        {"numero": "#42", "nome": "Doge", "descricao": "O carismático cão Shiba Inu que se tornou um dos memes mais atemporais da internet."},
        {"numero": "#43", "nome": "Óculos Deal With It", "descricao": "Os clássicos óculos escuros pixelados usados nos memes de superação."},
        {"numero": "#44", "nome": "Disquete", "descricao": "A antiga mídia física de armazenamento que virou o ícone universal de 'Salvar'."},
        {"numero": "#45", "nome": "Nokia 3310", "descricao": "O indestrutível celular lendário por sua resistência física e bateria infinita."}
    ],
    10: [
        {"numero": "#46", "nome": "Ada Lovelace", "descricao": "A matemática pioneira considerada a primeira programadora da história."},
        {"numero": "#47", "nome": "Alan Turing", "descricao": "O pai da ciência da computação e herói decodificador da máquina Enigma."},
        {"numero": "#48", "nome": "Linus Torvalds", "descricao": "O engenheiro de software criador do núcleo do Linux e da ferramenta Git."},
        {"numero": "#49", "nome": "Grace Hopper", "descricao": "A pioneira que criou o primeiro compilador e cunhou o termo 'bug'."},
        {"numero": "#50", "nome": "Comunidade Open Source", "descricao": "A força global de desenvolvedores que colaboram de graça para construir o futuro da tecnologia."}
    ]
}

# --- ENDPOINTS ---

# 1. GET "/" - Retorna uma mensagem de boas-vindas
@app.get("/")
def hello_world():
    # Retorna o dicionário que será convertido automaticamente para JSON pelo FastAPI
    return {"mensagem": "Bem-vindo ao álbum Copa do Mundo Geek/Nerd! 🤓"}

# 2. GET "/secoes" - Retorna a lista das 10 seções do álbum com validação Pydantic
@app.get("/secoes", response_model=List[Secao])
def listar_secoes():
    # Retorna todas as seções estáticas definidas no início do arquivo
    return SECOES_MOCK

# 3. GET "/secoes/{id}/figurinhas" - Retorna a lista de figurinhas de uma seção específica
@app.get("/secoes/{id}/figurinhas", response_model=List[Figurinha])
def listar_figurinhas(id: int):
    # Verifica se a seção com o id fornecido possui figurinhas mapeadas
    if id not in FIGURINHAS_MOCK:
        # Se não existir, retorna erro 404 (Não Encontrado) com uma mensagem explicativa
        raise HTTPException(status_code=404, detail="Seção não encontrada ou sem figurinhas.")
    
    # Retorna a lista de figurinhas associada à seção informada
    return FIGURINHAS_MOCK[id]
