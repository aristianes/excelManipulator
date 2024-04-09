import pandas as pd

dados = {
    'Nome': ['Maria', 'João', 'Ana'],
    'Idade': [25, 30, 28],
    'Profissão': ['Dentista','Maquinista', 'Frentista'],
    'Lazer': ['Caminhada',  'Ciclismo', 'Hipismo'],
    'Filiação': ['Carmem', 'Lucia', 'Eduardo']


}

df = pd.DataFrame(dados)
df.to_excel('exemplo.xlsx', index=False)
