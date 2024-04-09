import xlsxwriter

# Criar um novo arquivo Excel
workbook = xlsxwriter.Workbook('exemplo.xlsx')

# Adicionar uma nova planilha
worksheet = workbook.add_worksheet()

# Definir os cabeçalhos
cabecalhos = ['Nome', 'Idade']

# Escrever os cabeçalhos na primeira linha
for col, cabecalho in enumerate(cabecalhos):
    worksheet.write(0, col, cabecalho)

# Dados
dados = [
    ['João', 30],
    ['Maria', 25],
    ['Pedro', 35]
]

# Escrever os dados a partir da segunda linha
for linha, row_data in enumerate(dados, start=1):
    for col, cell_data in enumerate(row_data):
        worksheet.write(linha, col, cell_data)

# Fechar o arquivo Excel
workbook.close()
