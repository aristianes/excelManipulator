import random
import string

#Gera uma senha aleatória com o tamanho especificado.
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # join() para unir os caracteres selecionados em uma única string, que será nossa senha.
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha_gerada = gerar_senha(tamanho)
        print("Senha gerada:", senha_gerada)
    except ValueError:
        print("Erro: Entrada inválida! Certifique-se de digitar um número inteiro.")


