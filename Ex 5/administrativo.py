from funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        super().__init__(cpf, departamento, 10)

    def emprestar(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Funcionario administrativo do departamento "{}" pegou emprestado o livro: {} com {} dias de prazo'.format(self.departamento, titulo_do_livro, self.dias_de_emprestimo))

    def devolver(self, titulo_do_livro: str):
        if isinstance(titulo_do_livro, str):
            return ('Funcionario administrativo do departamento "{}" {}'.format(self.departamento, super().devolver(titulo_do_livro)))