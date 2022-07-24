class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def myFunc(self):
            print('Ola meu nome é ' + self.nome)

p1 = Pessoa('Gilberto', 37)
print('Nome:', p1.nome)
print('Idade:', p1.idade)

#del p1.idade

#print('Nome:', p1.nome)
#print('Idade:', p1.idade)

print(p1)
del p1
print(p1.nome)



