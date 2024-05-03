from bs4 import BeautifulSoup
import pandas as pd
import requests


def main():
    url_base = 'https://www.gunblood.com/gbscoresgd.php#google_vignette'
    response = requests.get(url_base)
    site = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todas as tabelas na página
    tables = site.find_all('table', attrs={'width': '100%', 'border': '0', 'align': 'center'})

    # Se houver pelo menos duas tabelas na página
    if len(tables) >= 2:
        # Processar a primeira tabela (últimos 7 dias)
        last_7_days_table = tables[0]
        df = process_table(last_7_days_table)
        df_relatorio = df.to_csv('teste7.csv')

        # Processar a segunda tabela (all time)
        all_time_table = tables[1]
        df = process_table(all_time_table)
        df_relatorio = df.to_csv('teste_all_time.csv')

    else:
        print("Erro: Não foram encontradas duas tabelas na página.")


def process_table(table):
    column_df = {
        'ranking': [],
        'player': [],
        'score': []
    }

    ranking = table.find_all('b')

    for rank in ranking:
        dado_rank = rank.text
        column_df['ranking'].append(dado_rank)

    div_scores = table.find_all('div', attrs={'align': 'center'})

    for div_score in div_scores:
        if div_score.find('b') is None:
            dado_score = div_score.text
            column_df['score'].append(dado_score)

    player_names = table.findAll('div', attrs={'align': 'left'})

    for player in player_names:
        dado_player = player.text
        column_df['player'].append(dado_player)

    df = pd.DataFrame(column_df)
    return df


if __name__ == '__main__':
    main()