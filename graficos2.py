import pandas as pd
import matplotlib.pyplot as plt

# Dados para a tabela
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Idade': [25, 30, 35, 40, 45],
    'Salário': [50000, 60000, 70000, 80000, 90000]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Criar um gráfico de barras com base nos dados de idade
plt.bar(df['Nome'], df['Idade'], color='skyblue')
plt.xlabel('Nome')
plt.ylabel('Idade')
plt.title('Idade por Nome')

# Adicionar uma tabela abaixo do gráfico
plt.table(cellText=df.values, colLabels=df.columns, loc='bottom')

# Ajustar o layout para que o gráfico e a tabela não se sobreponham
plt.subplots_adjust(left=0.2, bottom=0.2)

# Exibir o gráfico com a tabela
plt.show()
