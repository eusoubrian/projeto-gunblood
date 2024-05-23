from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime as datetime


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
    df['dat_ingestao'] = pd.to_datetime(datetime.datetime.now())
    return df

def write(df, assunto):
    path = f'datalake/{assunto}/file_{assunto}.xlsx' #TODO

    df.to_excel(
        path,
        index=False
    )