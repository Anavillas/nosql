from MODEL.livroBibliotecaModel import Livro, LivroModel

class LivroController:
    def __init__(self):
        self.model = LivroModel()

    def listar_livros(self):
        return self.model.listar_todos()

    def criar_livro(self, data):
        # Espera data = {"id": ..., "titulo": ..., "autor": ..., "genero": ..., "ano": ...}
        livro = Livro(
            lid=data["id"],  # Alterado de "pid" para "lid"
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        self.model.criar_livro(livro)

    def atualizar_livro(self, lid, data):
        livro = Livro(
            lid=lid,  # Alterado de "pid" para "lid"
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        return self.model.atualizar_livro(livro)

    def deletar_livro(self, lid):
        return self.model.deletar_livro(lid)  # Alterado de "pid" para "lid"
