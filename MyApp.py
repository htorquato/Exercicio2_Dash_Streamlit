# HELANO DUARTE TORQUATO¶
# Exercícios
# Utilize os arquivos do RECLAME AQUI e crie um dashboard com algumas caracteristicas.

# Empresas:

# Hapvida
# Nagem
# Ibyte
# O painel deve conter tais informações:

# Série temporal do número de reclamações.

# Frequência de reclamações por estado.

# Frequência de cada tipo de STATUS

# Distribuição do tamanho do texto (coluna DESCRIÇÃO)

# Alguns botões devem ser implementados no painel para operar filtros dinâmicos. Alguns exemplos::

# Seletor da empresa para ser analisada.

# Seletor do estado.

# Seletor por STATUS

# Seletor de tamanho do texto

# Faça o deploy da aplicação. Dicas:

# https://www.youtube.com/watch?v=vw0I8i7QJRk&list=PLRFQn2r6xhgcDMhp9NCWMqDYGfeeYsn5m&index=16&t=252s

# https://www.youtube.com/watch?v=HKoOBiAaHGg&t=515s

# Exemplo do github https://github.com/jlb-gmail/streamlit_teste

# OBSERVAÇÃO

# A resposta do exercicio é o link do github e o link da aplicação. Coloque-os abaixo.


# Importação das bibliotecas a serem usadas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px 


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

# Criando array com as Empresas para ser usado como seletor
df_Empresa=df_ra['EMPRESA'].unique()

# Criando array com os status para ser usado como seletor
df_status=df_ra['STATUS'].unique()

# Inserindo o título do App
st.title('Registro reclamações do Reclame Aqui')

with st.sidebar:
        UF_selecionada = st.selectbox('Estado',df_UF) 
        Empresa_Selecionada = st.selectbox('Empresa',df_Empresa)
        Status_Selecionado = st.selectbox('Status',df_status)

# Série temporal do número de reclamações
df_Temporal = df_ra.groupby(['TEMPO', 'EMPRESA']).size().reset_index(name='QTD')

# Reclamações por estado
# df_Qtd_UF = df_ra.groupby(['UF', 'EMPRESA']).size().reset_index(name='QTD')
df_Qtd_UF = df_ra[df_ra['STATUS']==Status_Selecionado].groupby(['UF', 'EMPRESA']).size().reset_index(name='QTD')

st.markdown('---')
# st.dataframe(df_ra[df_ra['UF'].isin(UF_selecionada)]
st.text('Série Temporal')
st.dataframe(df_Temporal[df_Temporal['EMPRESA']==Empresa_Selecionada])

st.markdown('---')
# Gráfico de barras com quantidade de casos por Estado
fig = px.bar(df_Qtd_UF[df_Qtd_UF['EMPRESA']==Empresa_Selecionada], x='UF', y='QTD')
fig

