class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def pega_saldo(self):
        return self.__saldo
    
    def devolve_titular(self):
        return self.__titular
    
    def retorna_limite(self):
        return self.__limite
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)




