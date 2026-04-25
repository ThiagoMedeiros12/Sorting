# 🔢 Sorting Algorithm Visualizer

> An interactive desktop application that animates classic sorting algorithms in real time, built with Python and CustomTkinter.

> Uma aplicação desktop interativa que anima algoritmos de ordenação clássicos em tempo real, construída com Python e CustomTkinter.

---

## 🇺🇸 English

### Overview

**Sorting Algorithm Visualizer** is a GUI application that lets you watch sorting algorithms work step-by-step through a smooth, colour-coded bar chart animation. It supports configurable array sizes and animation speeds, a live chronometer to track sorting duration, and playback controls (pause, resume, stop, reset).

### Features

- 📊 **Real-time visualisation** — each comparison and swap is rendered as a coloured frame on a canvas
- ⏱️ **Live chronometer** — tracks elapsed time from the moment sorting begins until it finishes
- ⚙️ **Configurable array size** — choose between 100, 500, or 1 000 elements
- 🚀 **Configurable speed**
  - **Very Fast** — targets ~500 rendered frames regardless of array size (uses stride skipping)
  - **60 FPS** — one frame every 16 ms
  - **30 FPS** — one frame every 33 ms
- ▶️ **Playback controls** — Generate, Start, Pause, Resume, Stop, Reset
- 🎨 **Colour coding**
  - 🔵 Blue — unsorted / idle bar
  - 🟡 Yellow — bars currently being *compared*
  - 🔴 Red — bars currently being *swapped*

### Algorithms implemented

| Algorithm    | Status      |
|--------------|-------------|
| Bubble Sort  | ✅ Complete  |

> More algorithms will be added in future releases.

### Project structure

```
Sorting/
├── main.py              # Application entry point
├── GUI/
│   └── gui.py           # MainApp & Visualizer (CustomTkinter UI + animation engine)
├── scripts/
│   └── script.py        # Array generation and sorting logic
├── pyproject.toml       # Project metadata and dependencies
└── README.md
```

### Requirements

- Python **3.13+**
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) **≥ 5.2.2**

### Installation & running

```bash
# 1. Clone the repository
git clone https://github.com/ThiagoMedeiros12/Sorting.git
cd Sorting

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install customtkinter

# 4. Run the application
python main.py
```

> **Tip:** If you use [`uv`](https://github.com/astral-sh/uv), you can simply run `uv run main.py` and dependencies will be handled automatically.

### How to use

1. Select an **Algorithm**, **Speed**, and **Array Size** from the dropdowns.
2. Click **Generate** to create a random, shuffled array.
3. Click **Start** to begin the animation.
4. Use **Pause / Resume** to halt and continue the animation at any point.
5. Click **Stop** to end the current run (time is preserved on screen).
6. Click **Reset** to clear the timer and return to the idle state.

---

## 🇧🇷 Português

### Visão geral

**Sorting Algorithm Visualizer** é uma aplicação GUI que permite acompanhar o funcionamento de algoritmos de ordenação passo a passo, por meio de uma animação suave e codificada por cores em um gráfico de barras. Suporta tamanhos de array configuráveis, velocidades de animação ajustáveis, um cronômetro ao vivo para medir o tempo de ordenação e controles de reprodução (pausar, retomar, parar, resetar).

### Funcionalidades

- 📊 **Visualização em tempo real** — cada comparação e troca é renderizada como um frame colorido no canvas
- ⏱️ **Cronômetro ao vivo** — registra o tempo decorrido desde o início até o fim da ordenação
- ⚙️ **Tamanho do array configurável** — escolha entre 100, 500 ou 1 000 elementos
- 🚀 **Velocidade configurável**
  - **Very Fast** — mira em ~500 frames renderizados independentemente do tamanho do array (usa salto de passos)
  - **60 FPS** — um frame a cada 16 ms
  - **30 FPS** — um frame a cada 33 ms
- ▶️ **Controles de reprodução** — Gerar, Iniciar, Pausar, Retomar, Parar, Resetar
- 🎨 **Codificação por cores**
  - 🔵 Azul — barra ociosa / não ordenada
  - 🟡 Amarelo — barras sendo *comparadas*
  - 🔴 Vermelho — barras sendo *trocadas*

### Algoritmos implementados

| Algoritmo    | Status       |
|--------------|--------------|
| Bubble Sort  | ✅ Completo   |

> Mais algoritmos serão adicionados em versões futuras.

### Estrutura do projeto

```
Sorting/
├── main.py              # Ponto de entrada da aplicação
├── GUI/
│   └── gui.py           # MainApp & Visualizer (UI CustomTkinter + motor de animação)
├── scripts/
│   └── script.py        # Geração de arrays e lógica de ordenação
├── pyproject.toml       # Metadados e dependências do projeto
└── README.md
```

### Requisitos

- Python **3.13+**
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) **≥ 5.2.2**

### Instalação e execução

```bash
# 1. Clone o repositório
git clone https://github.com/ThiagoMedeiros12/Sorting.git
cd Sorting

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate

# 3. Instale as dependências
pip install customtkinter

# 4. Execute a aplicação
python main.py
```

> **Dica:** Se você utiliza o [`uv`](https://github.com/astral-sh/uv), basta executar `uv run main.py` e as dependências serão gerenciadas automaticamente.

### Como usar

1. Selecione um **Algoritmo**, **Velocidade** e **Tamanho do Array** nos menus suspensos.
2. Clique em **Generate** para criar um array aleatório e embaralhado.
3. Clique em **Start** para iniciar a animação.
4. Use **Pause / Resume** para pausar e continuar a animação a qualquer momento.
5. Clique em **Stop** para encerrar a execução atual (o tempo permanece exibido na tela).
6. Clique em **Reset** para zerar o cronômetro e voltar ao estado inicial.

---


