class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'
    
class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    @property
    def listagem(self):
        return self._programa

    @property
    def tamanho(self):
        return len(self._programa)

  
  

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmemp = Filme('Todo mundo em panico', 1999, 130)
demolidor = Serie('Demolidor', 2016, 2)


vingadores.dar_likes()
tmemp.dar_likes()
vingadores.dar_likes()

demolidor.dar_likes()
atlanta.dar_likes()

filmes_e_series = [atlanta, vingadores, demolidor, tmemp]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

