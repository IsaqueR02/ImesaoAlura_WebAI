# Álbum de Figurinhas - Copa do Mundo Geek/Nerd 🤓✨

## Objetivo
O projeto consiste em um álbum de figurinhas digital, interativo e imersivo com a temática Geek/Nerd. Ele simula a sensação física de folhear um álbum de papel real através de efeitos sonoros sintetizados e uma mecânica de transição de páginas realista (com suporte para gestos e arrastes), permitindo que figurinhas sejam colecionadas e coladas nos slots apropriados de forma dinâmica através de uma API desenvolvida em FastAPI.

## Estrutura
O projeto está dividido entre Frontend (HTML/CSS/JS) e Backend (FastAPI em Python):
* **backend/**: Contém a API do servidor e a pasta de armazenamento das figurinhas.
* **frontend/**: Contém os arquivos da interface gráfica do álbum do usuário.

## O álbum
O álbum é composto por:
* **Páginas**: Capa, contracapa e 10 páginas temáticas (ex: Super-heróis, Fantasia & RPG, Ficção Científica, Animes, Jogos, etc.).
* **Slots**: Um total de 50 slots de figurinhas numeradas de `#01` a `#50`. Quando uma figurinha está colada, passar o cursor sobre ela revela curiosidades e a descrição sobre o personagem ou item correspondente.

## Sobre as imagens
* As imagens das figurinhas são servidas dinamicamente a partir do backend.
* Elas devem ser armazenadas na pasta `backend/figurinhas/` nomeadas com o padrão de prefixo numérico de dois dígitos correspondente ao seu ID (ex: `01-iron_man.jpg`, `02-batman.jpg`, `03-spider_man.jpg`, `04-wonder_woman.jpg` e `05-superman.jpg`).
* O servidor usa um sistema baseado em `glob` para encontrar a imagem correta correspondente ao ID da figurinha (prefixo `"{id:02d}[!0-9]*"`).

---

## Como rodar

### [backend/main.py](file:///c:/Users/VaioFE16/Documents/GitHub/ImesaoAlura_WebAI/backend/main.py)
O backend é uma API FastAPI que:
1. Inicia o servidor e monta o middleware CORS para permitir requisições de qualquer origem.
2. Contém uma lista chamada `figurinhas` com os 50 registros do álbum. Atualmente, os registros de ID 1 a 5 estão ativos (pois possuem imagens correspondentes na pasta) e os de ID 6 a 50 estão comentados no código.
3. Disponibiliza dois endpoints principais:
   * `GET /figurinhas`: Retorna os dados das figurinhas ativas no formato JSON.
   * `GET /figurinhas/{id}/imagem`: Retorna o arquivo de imagem correspondente utilizando busca de padrões por `glob`.

Para rodar o backend:
1. Abra um terminal e acesse a pasta `backend`:
   ```bash
   cd backend
   ```
2. Inicialize o servidor Uvicorn:
   ```bash
   .venv/Scripts/python -m uvicorn main:app --reload --port 8000
   ```

### [frontend/index.html](file:///c:/Users/VaioFE16/Documents/GitHub/ImesaoAlura_WebAI/frontend/index.html)
* Estrutura a visualização do álbum, organizando a capa, contracapa, páginas temáticas e os 50 slots onde as figurinhas são coladas de forma dinâmica via JavaScript ([app.js](file:///c:/Users/VaioFE16/Documents/GitHub/ImesaoAlura_WebAI/frontend/app.js)).

Para abrir o frontend:
* Basta dar dois cliques no arquivo [index.html](file:///c:/Users/VaioFE16/Documents/GitHub/ImesaoAlura_WebAI/frontend/index.html) para abri-lo diretamente no seu navegador, ou iniciá-lo por meio de um servidor estático como a extensão Live Server.

### [frontend/style.css](file:///c:/Users/VaioFE16/Documents/GitHub/ImesaoAlura_WebAI/frontend/style.css)
* Controla a identidade visual futurista e premium em tons escuros e violeta do álbum.
* Determina o tamanho físico dos slots regulares (`width: 227px`) e slots especiais ampliados (`width: 305.5px`).
* Estiliza as figurinhas coladas com efeito de fade-in animado (`sticker-img`).

---

## Controles
* **Navegação**: Para folhear as páginas do álbum, você pode usar os botões de seta lateral no ecrã, as teclas direcionais (ArrowLeft / ArrowRight) do teclado ou clicar e arrastar diretamente os cantos ou bordas das páginas.
* **Áudio**: Utilize o botão de controle de áudio no canto superior direito para ativar ou desativar os efeitos sonoros realistas de papel virando.
