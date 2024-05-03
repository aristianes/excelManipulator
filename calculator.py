def calculadora():
    #O while True é uma estrutura de controle em Python que cria um loop infinito.
    # Isso significa que o bloco de código dentro do while True será executado
    # repetidamente enquanto a condição True permanecer verdadeira.
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operador = input("Digite o operador (+, -, *, /): ")

            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
            else:
                print("Erro: Operador inválido!")
                continue

            print("Resultado:", resultado)
            break

        except ValueError:
            print("Erro: Entrada inválida! Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    calculadora()


