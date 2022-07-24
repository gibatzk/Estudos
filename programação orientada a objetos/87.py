class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def myFunc(self):
        print('Ola meu nome é ' + self.nome, 'e tenho', self.idade, 'de idade.')


p1 = Pessoa("Keila", 40)
p1.myFunc()

p2 = Pessoa("Keilla", 41)
p2.myFunc()
