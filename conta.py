


class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        print('Construindo...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do Titular {}'.format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor
        
    def transferir(self,valor, destino):
        self.saca(valor)
        destino.deposita(valor)