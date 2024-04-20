from funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        super().__init__(cpf, departamento, 20)

    def emprestar(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Professor do departamento "{}" pegou emprestado o livro: {} com {} dias de prazo'.format(self.departamento, titulo_do_livro, self.dias_de_emprestimo))

    def devolver(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Professor do departamento "{}" {}'.format(self.departamento, super().devolver(titulo_do_livro)))