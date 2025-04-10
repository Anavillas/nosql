from pymongo import MongoClient
from datetime import datetime

class userLivroBiblioteca:
    def __init__(self, eid, id_usuario, id_livro, nome_user, titulo_livro, data_emprestimo, data_devolucao):
        self.id = eid  
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.nome_user = nome_user
        self.titulo_livro = titulo_livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

class userLivroModel:
    
    def __init__(self, uri="mongodb://localhost:27017/", dbname="Biblioteca"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["userLivroBiblioteca"]

    def contar_emprestimos(self):

        return self.collection.count_documents({})

    def listar_emprestimos(self):

        cursor = self.collection.find({}, {"_id": 0})  
        return list(cursor)

    def criar_emprestimo(self, emprestimo: userLivroBiblioteca):
        doc = {
            "id": self.next_val(),  
            "id_usuario": emprestimo.id_usuario,
            "id_livro": emprestimo.id_livro,
            "nome_user": emprestimo.nome_user,
            "titulo_livro": emprestimo.titulo_livro,
            "data_emprestimo": emprestimo.data_emprestimo,
            "data_devolucao": emprestimo.data_devolucao
        }
        self.collection.insert_one(doc)

    def atualizar_emprestimo(self, emprestimo: userLivroBiblioteca):
       
        result = self.collection.update_one(
            {"id": emprestimo.id},  
            {"$set": {
                "id_usuario": emprestimo.id_usuario,
                "id_livro": emprestimo.id_livro,
                "nome_user": emprestimo.nome_user,
                "titulo_livro": emprestimo.titulo_livro,
                "data_emprestimo": emprestimo.data_emprestimo,
                "data_devolucao": emprestimo.data_devolucao
            }}
        )
        return result.modified_count 
    
    def deletar_emprestimo(self, eid: int):
        
        result = self.collection.delete_one({"id": eid})
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

    def listar_emprestimos_completo(self):
        
        pipeline = [
            {
                "$lookup": {
                    "from": "userBiblioteca",  
                    "localField": "id_usuario",  
                    "foreignField": "id", 
                    "as": "usuario_info"
                }
            },
            {
                "$lookup": {
                    "from": "livroBiblioteca",  
                    "localField": "id_livro",  
                    "foreignField": "id",  
                    "as": "livro_info"
                }
            },
            {
                "$unwind": "$usuario_info"  
            },
            {
                "$unwind": "$livro_info"  
            },
            {
                "$project": {
                    "id": 1,
                    "data_emprestimo": 1,
                    "data_devolucao": 1,
                    "usuario_nome": "$usuario_info.nome",  
                    "livro_titulo": "$livro_info.titulo",  
                    "livro_autor": "$livro_info.autor",   
                    "livro_genero": "$livro_info.genero",  
                    "livro_ano": "$livro_info.ano"         
                }
            }
        ]
        return list(self.collection.aggregate(pipeline))

    def buscar_emprestimo_por_id(self, eid: int):
        
        return self.collection.find_one({"id": eid}, {"_id": 0})
