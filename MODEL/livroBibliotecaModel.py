from pymongo import MongoClient


class LivroBiblioteca:
    
    def __init__(self, lid, titulo, autor, genero, ano):
        self.lid = lid
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano


class LivroModel:

    def __init__(self, uri="mongodb://localhost:27017/", dbname="Biblioteca"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["livroBiblioteca"]

    
    def contar_livros(self):
        return self.collection.count_documents({})

    def listar_todos(self):
        cursor = self.collection.find({}, {"_id": 0})  
        return list(cursor)

    def criar_livro(self, livro: LivroBiblioteca):
        doc = {
            "id": self.next_val(),  
            "titulo": livro.titulo,
            "autor": livro.autor,
            "genero": livro.genero,
            "ano": livro.ano
        }
        self.collection.insert_one(doc)

    def atualizar_livro(self, livro: LivroBiblioteca):
        result = self.collection.update_one(
            {"id": livro.lid},  
            {"$set": {
                "titulo": livro.titulo,
                "autor": livro.autor,
                "genero": livro.genero,
                "ano": livro.ano
            }}
        )
        return result.modified_count  

    def deletar_livro(self, lid: int):
        result = self.collection.delete_one({"id": lid})
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
