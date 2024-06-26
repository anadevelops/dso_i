from abc import ABC, abstractmethod

class UsuarioBU(ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo   

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf

    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo
    
    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo):
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo

    def emprestar(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('pegou emprestado o livro {} com {} dias de prazo'.format(titulo_do_livro, self.__dias_de_emprestimo))

    def devolver(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('devolveu o livro: {}'.format(titulo_do_livro))