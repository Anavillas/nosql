from MODEL.livroBibliotecaModel import LivroBiblioteca, LivroModel
from flask import jsonify


class LivroController:
    def __init__(self):
        self.model = LivroModel()
    
    def contar_livros(self):
        total = self.model.contar_livros()
        return jsonify({'total': total})

    def listar_livros(self):
        return self.model.listar_todos()

    def criar_livro(self, data):
        
        livro = LivroBiblioteca(
            lid=data["id"],  
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        self.model.criar_livro(livro)

    def atualizar_livro(self, lid, data):
        livro = LivroBiblioteca(
            lid=lid,  
            titulo=data["titulo"],
            autor=data["autor"],
            genero=data["genero"],
            ano=data["ano"]
        )
        return self.model.atualizar_livro(livro)

    def deletar_livro(self, lid):
        return self.model.deletar_livro(lid)  
