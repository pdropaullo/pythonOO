class Cliente(object):
    _nome = ""
    _telefone = ""
    _cidade = ""
    _idade = ""
    _sexo = ""

    def __init__(self, nome, telefone, cidade, idade, sexo):
        self._nome = nome
        self._telefone = telefone
        self._cidade = cidade
        self._idade = idade
        self._sexo = sexo

    def __str__(self):
        return "Obj Cliente: " + str(self._nome) + " - " + str(self._telefone) + " - " + str(
            self._cidade) + " - " + str(
            self._idade) + " anos - " + str(self._sexo)

    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome


cliente = Cliente("Pedro", "48 99136-7427", "São José", "29", "MASC")

print(cliente)
cliente.setNome("Paulo")
print(cliente.getNome())
