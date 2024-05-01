class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outra_pessoa):
        return self.idade == outra_pessoa.idade

    def __lt__(self, outra_pessoa):
        return self.idade < outra_pessoa.idade

# Exemplo de comparação de objetos de Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
print(pessoa1 == pessoa2)  # False
print(pessoa1 < pessoa2)   # False (compara pela idade)
