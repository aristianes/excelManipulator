import json

# Função para carregar as tarefas do arquivo JSON
def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Função para salvar as tarefas no arquivo JSON
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para adicionar uma nova tarefa à lista de tarefas
def adicionar_tarefa(titulo, descricao):
    tarefas = carregar_tarefas()
    nova_tarefa = {'titulo': titulo, 'descricao': descricao}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f'Tarefa "{titulo}" adicionada com sucesso!')

# Função para exibir todas as tarefas
def exibir_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print('Não há tarefas.')
    else:
        print('Lista de Tarefas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa["titulo"]}: {tarefa["descricao"]}')

# Adicionar algumas tarefas de exemplo
adicionar_tarefa('Comprar leite', 'Ir ao supermercado e comprar leite.')
adicionar_tarefa('Comprar coisas para viagem', 'bolacha, batata vinagre e sal,fone de ouvido')

# Exibir todas as tarefas
exibir_tarefas()
