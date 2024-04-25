class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outra):
        return self.idade == outra.idade

    def __lt__(self, outra):
        return self.idade < outra.idade

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print(pessoa1 == pessoa2)  # False
print(pessoa1 != pessoa2)  # True
print(pessoa1 < pessoa2)   # False
print(pessoa1 > pessoa2)   # True
