class Pessoa():
    def __init__(self, __nome, __idade):
        self.__nome = __nome
        self.__idade = __idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade


p1 = Pessoa("Ana", 21)
p2 = Pessoa("Ana", 21)
p3 = Pessoa("Giulia", 22)


print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p1 == p2)
print(p1)
print(p2)
print(id (p2))