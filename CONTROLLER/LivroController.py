from MODEL.livroBibliotecaModel import LivroBiblioteca, LivroModel

class LivroController:
    def __init__(self):
        self.model = LivroModel()

    def listar_livros(self):
        return self.model.listar_todos()

    def criar_livro(self, data):
        # Espera data = {"id": ..., "titulo": ..., "autor": ..., "genero": ..., "ano": ...}
        livro = LivroBiblioteca(
            lid=data["id"],  # Usando "lid" como identificador
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        self.model.criar_livro(livro)

    def atualizar_livro(self, lid, data):
        livro = LivroBiblioteca(
            lid=lid,  # Usando "lid" como identificador
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        return self.model.atualizar_livro(livro)

    def deletar_livro(self, lid):
        return self.model.deletar_livro(lid)  # Passando o "lid" para deletar
