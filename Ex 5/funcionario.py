from abc import ABC, abstractmethod
from usuariobu import UsuarioBU

class Funcionario(UsuarioBU):
    @abstractmethod
    def __init__(self, departamento, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        if departamento == 123123123:
            self.__departamento = 'INE'
        elif departamento == 321312312:
            self.__departamento = 'ADM'
        else:
            self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def emprestar(self, titulo_do_livro):
        if isinstance(titulo_do_livro, str):
            return ('do departamento "{}" pegou emprestado o livro: {} com {} dias de prazo'.format(self.departamento, titulo_do_livro, self.dias_de_emprestimo))
            
    def devolver(self, titulo_do_livro):
        if isinstance(titulo_do_livro, str):
            return (super().devolver(titulo_do_livro))
