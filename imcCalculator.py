#Calcula o Índice de Massa Corporal (IMC) com base no peso (em kg) e altura (em metros) fornecidos, ao quadrado.

def calculator_imc(peso , altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return " Sobrepeso"
    else:
        return "Obesidade"

if __name__ == "__main__":

    try:
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))
        imc = calculator_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        classificacao = classificar_imc(imc)
        print("Classificação:", classificacao)
    except ValueError:
        print("Erro: Entrada inválida! Certifique-se de digitar números válidos.")