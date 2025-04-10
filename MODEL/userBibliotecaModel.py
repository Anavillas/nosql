from pymongo import MongoClient

class userBiblioteca:
    
    def __init__(self, uid, nome, fone):
        self.uid = uid
        self.nome = nome
        self.fone = fone

class userModel:
    
    def __init__(self, uri="mongodb://localhost:27017/", dbname="Biblioteca"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["userBiblioteca"]

    def contar_users(self):
        return self.collection.count_documents({})
    
    def listar_todos(self):
        cursor = self.collection.find({}, {"_id": 0}) 
        return list(cursor)

    def criar_user(self, user: userBiblioteca):
        doc = {
            "id": self.next_val(),  
            "nome": user.nome,
            "fone": user.fone
        }
        self.collection.insert_one(doc)

    def atualizar_user(self, user: userBiblioteca):
        result = self.collection.update_one(
            {"id": user.uid},  
            {"$set": {
                "nome": user.nome,
                "fone": user.fone
            }}
        )
        return result.modified_count 

    def deletar_user(self, uid: int):
        result = self.collection.delete_one({"id": uid})
        return result.deleted_count 
    
    def obter_maior_id(self):
        doc = self.collection.find({}, {"_id": 0, "id": 1}) \
                             .sort("id", -1) \
                             .limit(1)
        lista = list(doc)
        if not lista:
            return 0  
        return lista[0]["id"]
    
    def next_val(self):
        return self.obter_maior_id() + 1