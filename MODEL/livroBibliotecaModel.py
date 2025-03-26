# livroBibliotecaModel.py
from pymongo import MongoClient

class livroBiblioteca:
    """Entidade que representa uma Pessoa."""
    def __init__(self, pid, titulo, autor, genero, ano):
        self.pid = pid
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano


class livroModel:
    """Classe responsável pela persistência de dados de Pessoa no MongoDB."""
    def __init__(self, uri="mongodb://localhost:27017/", dbname="Biblioteca"):
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["livroBiblioteca"]

    def listar_todos(self):
        cursor = self.collection.find({}, {"_id": 0})
        return list(cursor)

    def criar_livro(self, livro: livroBiblioteca):
        doc = {
            "id": self.next_val(),
            "titulo": livro.titulo,
            "autor": livro.autor,
            "genero": livro.genero,
            "ano": livro.ano

        }
        self.collection.insert_one(doc)

    def atualizar_livro(self, livro: livroBiblioteca):
        result = self.collection.update_one(
            {"id": livro.pid},
            {"$set": {
                "titulo": livro.titulo,
                "autor": livro.autor,
                "genero": livro.genero,
                "ano": livro.ano
            }}
        )
        return result.modified_count  # 0 ou 1

    def deletar_pessoa(self, pid: int):
        result = self.collection.delete_one({"id": pid})
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
