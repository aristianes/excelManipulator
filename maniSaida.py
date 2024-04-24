import sys

#é um objeto que representa a saída padrão do sistema.
# Por padrão, quando você usa funções de saída como print(),
# os resultados são enviados para sys.stdout, que normalmente está associado à tela.
# No entanto, você pode redirecionar sys.stdout para enviar a saída para outros dispositivos,
# como um arquivo, se desejar gravar a saída em um local diferente.


with open('saida.txt', 'w') as arquivo:
    sys.stdout = arquivo
    print(" Este texto sera escrito em 'saida.txt'.")