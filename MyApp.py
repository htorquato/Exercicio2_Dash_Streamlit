# import streamlit as st
# import pandas as pd

# st.write("""
# My first app
# Hello *world*
# """)

# # df = pd.read_csv('winequality-red.csv')
# # st.line_chart(df)

# options = st.multiselect(
#     'Selecione os estados',
#     ['PE', 'BA', 'GO', 'CE', 'SP', 'MA', 'PA', 'AL', 'RN', 'PB', '--',
#        'MS', 'ES', 'AM', 'MT', 'SE', 'MG', 'RS', 'RR', 'RJ', 'SC', 'PI',
#        'TO', 'DF', 'PR', 'AP', 'ta', ' P', ' C'],
#     ['PE', 'BA', 'GO', 'CE', 'SP', 'MA', 'PA', 'AL', 'RN', 'PB',
#        'MS', 'ES', 'AM', 'MT', 'SE', 'MG', 'RS', 'RR', 'RJ', 'SC', 'PI',
#        'TO', 'DF', 'PR', 'AP'])

# st.write('You selected:', options)

# st.write ('Teste')


# Importação das bibliotecas a serem usadas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Importação dos datasets a serem usados
df_nagem=pd.read_csv('RECLAMEAQUI_NAGEM.csv')
df_hapvida=pd.read_csv('RECLAMEAQUI_HAPVIDA.csv')
df_ibyte=pd.read_csv('RECLAMEAQUI_IBYTE.csv')

# Adicionando coluna com o nome da empresa
df_hapvida['EMPRESA']='Hapvida'
df_ibyte['EMPRESA']='ibyte'
df_nagem['EMPRESA']='Nagem'

# Concatenar os datafrmaes
df_ra = pd.concat([df_hapvida, df_ibyte, df_nagem])

# Adicionando a coluna UF com o conteúdo das 2 últimas posições da coluna LOCAL
df_ra['UF'] = df_ra['LOCAL'].str[-2:]

# Alterando para data o tipo da coluna TEMPO
df_ra['TEMPO']=pd.to_datetime(df_ra['TEMPO'])

# Criando array com as UFs para ser usado como seletor
df_UF=df_ra['UF'].unique()

# Inserindo o título do App
st.title('Registro reclamações do Reclame Aqui')

with st.sidebar:
        UF =st.multiselect('Selecione os estados',df_UF,df_UF)

