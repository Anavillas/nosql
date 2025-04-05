from MODEL.userBibliotecaModel import userBiblioteca, userModel

class UserController:
    def __init__(self):
        self.model = userModel()

    def listar_users(self):
        return self.model.listar_todos()

    def criar_user(self, data):
        # Espera data = {"id": ..., "nome": ..., "nome": ..., "genero": ..., "ano": ...}
        user = userBiblioteca(
            uid=data["id"],  # Usando "uid" como identificador
            nome=data["nome"],
            fone=data["fone"]
        )
        self.model.criar_user(user)

    def atualizar_user(self, uid, data):
        user = userBiblioteca(
            uid=uid,  # Usando "uid" como identificador
            nome=data["nome"],
            fone=data["fone"]
        )
        return self.model.atualizar_user(user)

    def deletar_user(self, uid):
        return self.model.deletar_user(uid)  # Passando o "uid" para deletar
