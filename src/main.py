from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime as datetime
from config import helpers

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
        df = helpers.process_table(last_7_days_table)
        assunto = 'sete_dias'
        helpers.write(df, assunto)

        # Processar a segunda tabela (all time)
        all_time_table = tables[1]
        df = helpers.process_table(all_time_table)
        assunto = 'all_time'
        helpers.write(df, assunto)

    else:
        print("Erro: Não foram encontradas duas tabelas na página.")


if __name__ == '__main__':
    main()