import sys

#é um objeto que representa a entrada padrão do sistema.
# Em um ambiente de terminal, por exemplo, sys.stdin é associado ao teclado.
# Isso significa que, por padrão, quando você chama funções de entrada como input(),
# o Python espera que você digite dados do teclado.
# No entanto, você pode redirecionar sys.stdin para ler dados de outros dispositivos,
# como um arquivo, se desejar processar dados de entrada de uma fonte diferente do teclado.

with open('teste.txt', 'r') as arquivo:
    sys.stdin = arquivo
    for linha in sys.stdin:
        print(linha.strip())
