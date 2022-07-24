class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dadosCompleto(self):
        print(self.nome, self.sobrenome, self.idade)

#p1 = Pessoa('Gilberto', 'Tezuka', 36)
#p1.dadosCompleto()

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, idade):
        #Pessoa.__init__(self, nome, sobrenome, idade)
        super().__init__(nome, sobrenome, idade)

p1 = Estudante('Gilberto', 'Tezuka', 37)
p1.dadosCompleto()
