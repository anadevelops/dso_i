from abc import ABC, abstractmethod
from usuariobu import UsuarioBU

class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, str):
            self.__matricula = matricula

    def emprestar(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Aluno de matricula "{}" pegou emprestado o livro: {} com {} dias de prazo'.format(self.matricula, titulo_do_livro, self.dias_de_emprestimo))

    def devolver(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Aluno de matricula "{}" devolveu o livro: {}'.format(self.matricula, titulo_do_livro))