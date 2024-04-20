from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(ano, int):
            self.__ano = ano
        if isinstance(editora, Editora):
            self.__editora = editora
        self.__autores = []
        self.__capitulos = []

        if isinstance(autor, Autor):
            self.__autores.append(autor)

        capitulo = Capitulo(numero_capitulo, titulo_capitulo)
        if isinstance(capitulo, Capitulo):
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
        return [autor.nome for autor in self.__autores]

    @property
    def capitulos(self):
        return [ capitulo.titulo for capitulo in self.__capitulos]
    
    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            for aut in self.__autores:
                if aut.codigo == autor.codigo:
                    break
                else:
                    self.__autores.append(autor)
                    break

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            for aut in self.__autores:
                if aut.codigo == autor.codigo:
                    self.__autores.remove(autor)
                    break

    def incluir_capitulo(self, numero_capitulo: int, titulo_capitulo: str):
        if self.find_capitulo_by_titulo(titulo_capitulo) == None:
            self.__capitulos.append(Capitulo(numero_capitulo, titulo_capitulo))
    
    def excluir_capitulo(self, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if capitulo != None:
            self.__capitulos.remove(capitulo)


    def find_capitulo_by_titulo(self, titulo: str):
        for i in self.__capitulos:
            if i.titulo == titulo:
                return i
        return None
    