from pymongo import MongoClient

class UserBiblioteca:
    """Entidade que representa um user."""
    def __init__(self, uid, nome, fone):
        self.uid = uid
        self.nome = nome
        self.fone = fone

class UserModel:
    """Classe responsável pela persistência de dados de user no MongoDB."""
    def __init__(self, uri="mongodb://localhost:27017/", dbname="Biblioteca"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["userBiblioteca"]

    def listar_todos(self):
        cursor = self.collection.find({}, {"_id": 0})  # Excluindo o _id no retorno
        return list(cursor)

    def criar_user(self, user: UserBiblioteca):
        doc = {
            "id": self.next_val(),  # Usando next_val para garantir que o id seja único e sequencial
            "nome": user.nome,
            "fone": user.fone
        }
        self.collection.insert_one(doc)

    def atualizar_user(self, user: UserBiblioteca):
        result = self.collection.update_one(
            {"id": user.uid},  # Usando 'id' para encontrar o user
            {"$set": {
                "nome": user.nome,
                "fone": user.fone
            }}
        )
        return result.modified_count  # 0 ou 1

    def deletar_user(self, uid: int):
        result = self.collection.delete_one({"id": uid})
        return result.deleted_count  # 0 ou 1
    
    def obter_maior_id(self):
        doc = self.collection.find({}, {"_id": 0, "id": 1}) \
                             .sort("id", -1) \
                             .limit(1)
        lista = list(doc)
        if not lista:
            return 0  # Se não há documentos, retornamos 0
        return lista[0]["id"]
    
    def next_val(self):
        return self.obter_maior_id() + 1
