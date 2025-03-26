from flask import Blueprint, request, jsonify
from CONTROLLER.LivroController import LivroController

livro_bp = Blueprint("livro_bp", __name__)
livroController = LivroController()

# GET /livros
@livro_bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = livroController.listar_livros()
    return jsonify(livros), 200

# POST /livros
@livro_bp.route("/livros", methods=["POST"])
def criar_livro():
    data = request.json  # Ex.: {"id": int, "titulo": str, "autor": str, "genero": str, "ano": int}
    livroController.criar_livro(data)
    return jsonify({"mensagem": "Livro inserido com sucesso!"}), 201

# PUT /livros/<lid>
@livro_bp.route("/livros/<int:lid>", methods=["PUT"])
def atualizar_livro(lid):
    data = request.json
    mod_count = livroController.atualizar_livro(lid, data)
    if mod_count == 0:
        return jsonify({"erro": "Livro não encontrado!"}), 404
    return jsonify({"mensagem": "Livro atualizado com sucesso!"}), 200

# DELETE /livros/<lid>
@livro_bp.route("/livros/<int:lid>", methods=["DELETE"])
def deletar_livro(lid):
    del_count = livroController.deletar_livro(lid)
    if del_count == 0:
        return jsonify({"erro": "Livro não encontrado!"}), 404
    return jsonify({"mensagem": "Livro deletado com sucesso!"}), 200
