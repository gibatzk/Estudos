class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def myFunc(self):
            print('Ola meu nome é ' + self.nome)

p1 = Pessoa('Gilberto', 37)
p1.myFunc()

p1.nome = 'Lillian'
p1.myFunc()