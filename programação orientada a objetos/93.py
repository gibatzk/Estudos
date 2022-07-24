class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dadosCompleto(self):
        print(self.nome, self.sobrenome, self.idade)

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome, idade, anoGraduação):
        super().__init__(nome, sobrenome, idade)
        self.anoGraduação = anoGraduação

    def bemVindo(self):
        print('Bem vindo ', self.nome, self.sobrenome, self.idade, 'anos de idade,', 'se forma em ', self.anoGraduação, 'em Ciência de Dados')

x = Estudante('Gilberto', 'Tezuka', 37, 2024)
x.dadosCompleto()
x.bemVindo()
#print(x.anoGraduação)