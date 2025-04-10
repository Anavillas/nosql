from MODEL.userBibliotecaModel import userBiblioteca, userModel
from flask import jsonify

class UserController:
    def __init__(self):
        self.model = userModel()

    def contar_users(self):
        total = self.model.contar_users()
        return jsonify({'total': total})
    
    def listar_users(self):
        return self.model.listar_todos()

    def criar_user(self, data):
        
        user = userBiblioteca(
            uid=data["id"], 
            nome=data["nome"],
            fone=data["fone"]
        )
        self.model.criar_user(user)

    def atualizar_user(self, uid, data):
        user = userBiblioteca(
            uid=uid,  
            nome=data["nome"],
            fone=data["fone"]
        )
        return self.model.atualizar_user(user)

    def deletar_user(self, uid):
        return self.model.deletar_user(uid)  
