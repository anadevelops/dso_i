from editora import Editora
from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

ed1 = Editora(1, 'ana')
au1 = Autor(1, 'thais')
liv1 = Livro(10, 'karen', 2024, ed1, au1, 5, 'karen elaine')
au2 = Autor(2, 'kiki')
b1 = Biblioteca()
b1.incluir_livro(liv1)
print('liv1: ' + liv1.titulo)
print(b1.livros)

liv2 = Livro(5, 'anaa', 2024, ed1, au2, 10, 'ana crara')
b1.incluir_livro(liv2)
print('liv2: ' + liv2.titulo)
print(b1.livros)


liv1.incluir_capitulo(2, 'bud')
liv1.incluir_autor(au2)

print(liv1.autores)
print(liv1.capitulos)

print(liv1.find_capitulo_by_titulo('bud'))



