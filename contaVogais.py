
#o def indica a criacao de uma funcao

def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    #aqui a variavel char e somente o copinho que pega agua no balde e ela so vale dentro do escopo do for
    for char in string:
        if char in vogais:
            contador += 1
    return contador

if __name__ == "__main__":
    entrada = input("Digite uma string: ")
    numero_vogais = contar_vogais(entrada)
    print("Número de vogais na string:", numero_vogais)
