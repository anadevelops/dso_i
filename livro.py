from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.__capitulos = []

        self.__autores.append(autor)

        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos.append(capitulo)

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano   

    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, editora):
        if isinstance(editora, Editora):
            self.__editora = editora 

    @property
    def autores(self):
        return self.__autores
    
    def incluir_autor(self, autor: Autor):
        self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor.nome in self.__autores:
            for i in self.__autores:
                if i.nome == autor.nome:
                    self.__autores.pop(i)

    def incluir_capitulo(self, numero_capitulo: int, titulo_capitulo: str):
        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        self.__capitulos.append(capitulo)

    def excluir_capitulo(self, titulo: str):
        #if titulo in self.__capitulos.titulo:
            for i in self.__capitulos:
                if i.titulo == titulo:
                    self.__capitulos.pop(i)

    def find_capitulo_by_titulo(self, titulo: str):
        for i in self.__capitulos:
            if i.titulo == titulo:
                return i