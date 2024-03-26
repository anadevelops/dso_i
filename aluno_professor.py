class Endereco:
    def __init__(self, cidade: str, estado: str):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

class Pessoa:
    def __init__(self, nome, cidade, estado):
        self.__nome = nome
        self.__endereco = Endereco(cidade, estado)

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class Aluno(Pessoa):
    def __init__(self, nome, cidade, estado):
        super().__init__(nome, cidade, estado)

class Professor(Pessoa):

    def __init__(self, orientando: Aluno, nome, cidade, estado):
        super().__init__(nome, cidade, estado)
        self.__orientando = orientando

    @property
    def orientando(self):
        return self.__orientando

    @orientando.setter
    def orientando(self, orientando):
        self.__orientando = orientando

a1 = Aluno("Ana", 'Jlle', 'SC')
p1 = Professor(a1, 'Thais', 'Floripa', 'SC')
print(a1.nome)
print(p1.orientando.nome)

print(a1.endereco.cidade)
print(p1.endereco.estado)