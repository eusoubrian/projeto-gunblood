# 🔫 GunBlood Web Scraper & Dashboard

Este projeto utiliza web scraping para extrair dados de tabelas de ranking de um jogo, processa esses dados e exibe-os em um dashboard interativo usando Plotly e Streamlit.

<img src="img\gunblood.jpg" alt="Descrição da imagem">

## 📃 URL do top 200
    https://www.gunblood.com/gbscoresgd.php

## 📋 Descrição

O projeto tem dois componentes principais:
1. **Web Scraping**: Extrai os dados das tabelas de ranking de um site de jogos e os armazena em arquivos Excel.
2. **Dashboard**: Usa Streamlit e Plotly para visualizar os dados em um dashboard interativo.

## 🚀 Como Usar

### Clonando o Repositório

1. Clone este repositório:

    ```bash
    git clone https://github.com/eusoubrian/projeto-gunblood.git
    cd projeto-gunblood
    ```

### Executando o Web Scraper

3. Execute o script de web scraping:

    ```bash
    python main.py
    ```

### Executando o Dashboard

4. Execute o dashboard:

    ```bash
    streamlit run dashboard.py
    ```