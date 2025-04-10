from flask import Blueprint, request, jsonify
from CONTROLLER.UserController import UserController

user_bp = Blueprint("user_bp", __name__)
userController = UserController()

# GET /users
@user_bp.route("/users", methods=["GET"])
def listar_users():
    users = userController.listar_users()
    return jsonify(users), 200

# POST /users
@user_bp.route("/users", methods=["POST"])
def criar_user():
    data = request.json  # Ex.: {"id": int, "titulo": str, "autor": str, "genero": str, "ano": int}
    userController.criar_user(data)
    return jsonify({"mensagem": "user inserido com sucesso!"}), 201

# PUT /users/<uid>
@user_bp.route("/users/<int:uid>", methods=["PUT"])
def atualizar_user(uid):
    data = request.json
    mod_count = userController.atualizar_user(uid, data)
    if mod_count == 0:
        return jsonify({"erro": "user não encontrado!"}), 404
    return jsonify({"mensagem": "user atualizado com sucesso!"}), 200

# DELETE /users/<uid>
@user_bp.route("/users/<int:uid>", methods=["DELETE"])
def deletar_user(uid):
    del_count = userController.deletar_user(uid)
    if del_count == 0:
        return jsonify({"erro": "user não encontrado!"}), 404
    return jsonify({"mensagem": "user deletado com sucesso!"}), 200

@user_bp.route("/contar-users", methods=["GET"])
def contar_users():
    return userController.contar_users()