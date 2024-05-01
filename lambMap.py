numeros = [10, 22, 33, 44, 55]

# Usando uma expressão lambda com a função map() para calcular o quadrado de cada número

quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [100, 484, 1089, 1936, 3025]

