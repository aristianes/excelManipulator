import pandas as pd

# Carregar a planilha Excel em um DataFrame do pandas
dados_excel = pd.read_excel('exemplo.xlsx', usecols=['Nome'])

# Exibir os dados da coluna 'Nome'
print(dados_excel['Nome'])




