class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoas = [
    Pessoa("Alice", 30),
    Pessoa("Bob", 25),
    Pessoa("Charlie", 35)
]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa.idade)
print("Pessoas ordenadas por idade:")
for pessoa in pessoas_ordenadas:
    print(pessoa.nome, pessoa.idade)
