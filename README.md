# Alura Album - Copa do Mundo Geek/Nerd (Frontend)

Este é o repositório do frontend do projeto **Alura Album - Copa do Mundo Geek/Nerd**, desenvolvido durante a Imersão AI da Alura. O projeto consiste em um álbum de figurinhas digital e interativo com temática geek, pop e nerd, homenageando grandes personagens de ficção, animes, jogos, memes, e celebridades da comunidade (dubladores, cantores e influenciadores).

---

## 🎯 Objetivo do Projeto

Proporcionar uma experiência interativa e imersiva de colecionar figurinhas digitais. Ele simula o folhear físico de um álbum de papel diretamente no navegador com 12 páginas (Capa, Contracapa e 10 páginas internas) contendo 50 figurinhas colecionáveis. Possui efeitos de som realistas de virada de página e um sistema interativo onde passar o mouse sobre as figurinhas já coladas revela curiosidades sobre o personagem ou item correspondente.

---

## 📂 Funcionalidade dos Arquivos

### 1. 📄 [index.html](file:///c:/Users/VaioFE16/Desktop/Alura_ImersionAI/ImesaoAlura_frontend/index.html)
* **Estrutura e Conteúdo**: Define o esqueleto HTML do álbum.
* **Seções do Álbum**: Contém a capa personalizada ("ALURA GEEK/NERD") e 10 páginas temáticas divididas por categorias Geek/Nerd:
  1. *Super-heróis*
  2. *Fantasia & RPG*
  3. *Ficção Científica*
  4. *Anime & Mangá - Clássicos*
  5. *Anime & Mangá - Nova Geração*
  6. *Jogos & Games*
  7. *Celebridades (Atores & Dubladores)*
  8. *Música & Trilhas*
  9. *Gadgets, Símbolos & Memes*
  10. *Criadores & Comunidade*
* **Slots das Figurinhas**: Define a posição de cada uma das 50 figurinhas com seu número identificador (ex: `#01 Homem de Ferro`).
* **Componentes de Controle**: Inclui os botões de navegação lateral (Próxima Página e Página Anterior) e o controle mutador de efeitos sonoros.

### 2. 🎨 [style.css](file:///c:/Users/VaioFE16/Desktop/Alura_ImersionAI/ImesaoAlura_frontend/style.css)
* **Estilização e Tema**: Define a identidade visual futurista e premium (escura, com gradientes radiais, tons de roxo e violeta).
* **Efeitos Visuais**: Implementa o efeito *glitch* nos textos da capa, sombras realistas de lombada nas dobras das páginas, e animação de rotação da esfera central.
* **Badges Temáticas**: Estiliza os badges de cada categoria do álbum com a nova paleta de cores.
* **Curiosidades no Hover (Tooltip)**: Controla a exibição interativa do texto de descrição/curiosidade (`.slot-role`) quando o usuário passa o mouse por cima de uma figurinha já colada (`.slot-preenchido`), criando um overlay semitransparente sobre a figurinha.

### 3. ⚡ [app.js](file:///c:/Users/VaioFE16/Desktop/Alura_ImersionAI/ImesaoAlura_frontend/app.js)
* **Integração com Backend**: Realiza chamadas assíncronas para a API local (`http://localhost:8000/figurinhas`) para carregar dinamicamente as figurinhas do ID 1 ao 50 nos slots correspondentes.
* **Controle da Biblioteca PageFlip**: Inicializa e configura o `St.PageFlip` para lidar com a física de virada das páginas de forma automatizada e com suporte a arraste e gestos mobile.
* **Controle de Áudio**: Lida com a geração sintetizada de som (Web Audio API) de papel virando para cada troca de página.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5** para estruturação semântica.
* **CSS3** para o design moderno em tons de roxo/violeta, tooltips interativos e micro-animações.
* **JavaScript (ES6+)** para manipulação do DOM, controle de áudio sintetizado e consumo de APIs.
* **St.PageFlip** (biblioteca externa de paginação de livros).
