import streamlit as st
import pandas as pd
import plotly.express as px


def main():

    st.set_page_config(
        page_title='Dashboard Rank GunBlood',
        page_icon='chart_with_upwards_trend',
        layout='wide'
    )

    st.title('Dashboard Rank GunBlood')

    path_all_time = 'datalake/all_time/file_all_time.xlsx'

    df_all_time = pd.read_excel(path_all_time)
    
    df = valida_tipos(df_all_time)

    st.write(df)

    # Calcular a média de score
    media_score = df['SCORE'].mean()

    contagem = df['PLAYER'].value_counts()

    # Exibir a KPI da média de score
    st.markdown(f'## Média de Score\n\n ### {media_score}', unsafe_allow_html=True)


def valida_tipos(df):

    df = df[['ranking', 'player', 'score']]

    df['ranking'] = df['ranking'].astype(int)
    df['player'] = df['player'].astype(str)
    df['score'] = df['score'].astype(int)
    
    df = df.rename(columns={
        'ranking': 'RANK',
        'player': 'PLAYER',
        'score': 'SCORE'
    })

    return df





if __name__ == "__main__":
    main()