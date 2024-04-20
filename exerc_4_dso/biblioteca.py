from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            if len(self.__livros) > 0:
                for liv in self.__livros:
                    if liv.codigo == livro.codigo:
                        break
                    else:
                        self.__livros.append(livro)
                        break
            else:
                self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
            if len(self.__livros) > 1:
                for liv in self.__livros:
                    if liv == livro:
                        self.__livros.remove(livro)
                        break
                    else:
                        break
            else:
                self.__livros.remove(livro)

    @property
    def livros(self):
        return [livro.titulo for livro in self.__livros]

