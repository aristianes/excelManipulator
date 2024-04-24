import sys

# é um objeto que representa a saída de erro padrão do sistema.
# Ele é usado para mensagens de erro e normalmente está associado à tela, assim como sys.stdout.
# Assim como sys.stdout,você pode redirecionar sys.stderr para enviar mensagens de erro para outros dispositivos,
# se desejar.


with open('erros.txt', 'w') as arquivo:
    sys.stderr = arquivo
    print("Este é um erro que será escrito em 'erros.txt'.", file=sys.stderr)
