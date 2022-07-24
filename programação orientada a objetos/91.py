class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dadosCompleto(self):
        print(self.nome, self.sobrenome, self.idade)

p1 = Pessoa('Gilberto', 'Tezuka', 36)
p1.dadosCompleto()

class Estudante(Pessoa):
    pass

p2 = Estudante('Lillian', 'Duarte', 38)
p2.dadosCompleto()