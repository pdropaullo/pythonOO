# 1 - criando a classe ----------------------------------------------
class Carro:

    # 2 - definindo o método construtor -----------------------------
    def __init__(self, modelo, preco):
        self._modelo = "2010"
        self._preco = preco

    # metodo getter para modelo
    @property
    def modelo(self):
        return self._modelo


    # metodo setter para modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    # método que retorna as informações do objeto em string...
    def __str__(self):
        return "Obj Carro "+str(self.modelo) + " - " + str(self.preco)

objCarro = Carro('2012',23489.90)       # cria o objeto, necessário para acessar os metodos e atributos da classe
objCarro.preco = 123444.00              # - setando um novo preço
print(objCarro)                         #  exibindo os dados do objeto


