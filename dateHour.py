import datetime

# Obtendo a data e hora atuais
agora = datetime.datetime.now()
print("Data e hora atuais:", agora)

# Criando um objeto de datetime específico
data_hora = datetime.datetime(2022, 4, 15, 12, 30, 0)
print("Data e hora específicas:", data_hora)

# Acessando os componentes de data e hora separadamente
print("Ano:", agora.year)
print("Mês:", agora.month)
print("Dia:", agora.day)
print("Hora:", agora.hour)
print("Minuto:", agora.minute)
print("Segundo:", agora.second)
print("Microssegundo:", agora.microsecond)
