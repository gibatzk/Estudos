def JogoDaVelha():
  tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  def ImprimirTabuleiro():
    print()
    print('', tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---|---|---")
    print('', tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---|---|---")
    print('', tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

  ImprimirTabuleiro()

JogoDaVelha()