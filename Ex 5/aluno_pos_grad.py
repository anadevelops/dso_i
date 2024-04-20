from aluno import Aluno

class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False
        #if self.__elaborando_tese is True:
            #self.dias_de_emprestimo = 2 * self.dias_de_emprestimo

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, tese):
        if isinstance(tese, bool):
            if tese is True:
               self.dias_de_emprestimo = self.dias_de_emprestimo * 2
               self.__elaborando_tese = tese
            else:
                self.__elaborando_tese = tese

    def emprestar(self, titulo_do_livro):
        if isinstance(titulo_do_livro, str):
            return (super().emprestar(titulo_do_livro))

    def devolver(self, titulo_do_livro):
        if isinstance(titulo_do_livro, str):
            return (super().devolver(titulo_do_livro))