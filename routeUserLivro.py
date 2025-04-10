from flask import Blueprint, request, jsonify
from CONTROLLER.UserLivroController import UserLivroBibliotecaController

# Criando o Blueprint para o Empréstimo de Livros
emprestimo_bp = Blueprint("emprestimo_bp", __name__)

# Inicializando o controlador
userLivroBibliotecaController = UserLivroBibliotecaController()

# Rota para contar o total de empréstimos de livros
@emprestimo_bp.route("/count", methods=["GET"])
def contar_emprestimos():
    return userLivroBibliotecaController.contar_emprestimos()

# Rota para listar todos os empréstimos de livros
@emprestimo_bp.route("/emprestimos-livros", methods=["GET"])
def listar_emprestimos():
    return userLivroBibliotecaController.listar_emprestimos()

# Rota para criar um novo empréstimo de livro
@emprestimo_bp.route("/emprestimos-livros", methods=["POST"])
def criar_emprestimo():
    return userLivroBibliotecaController.criar_emprestimo()

# Rota para atualizar um empréstimo de livro
@emprestimo_bp.route("/emprestimos-livros/<int:eid>", methods=["PUT"])
def atualizar_emprestimo(eid):
    return userLivroBibliotecaController.atualizar_emprestimo(eid)

# Rota para deletar um empréstimo de livro
@emprestimo_bp.route("/emprestimos-livros/<int:eid>", methods=["DELETE"])
def deletar_emprestimo(eid):
    return userLivroBibliotecaController.deletar_emprestimo(eid)
