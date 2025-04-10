from flask import jsonify, request
from datetime import datetime
from MODEL.userLivroBiblioteca import userLivroBiblioteca, userLivroModel

class UserLivroBibliotecaController:
    

    def __init__(self):
        self.model = userLivroModel()

    def contar_emprestimos(self):
        
        total = self.model.contar_emprestimos()
        return jsonify({'total': total})

    def listar_emprestimos(self):
        
        emprestimos = self.model.listar_emprestimos()
        return jsonify(emprestimos)

    def criar_emprestimo(self):
       
        data = request.get_json()  
        
        try:
            data_emprestimo = datetime.strptime(data["data_emprestimo"], "%Y-%m-%d")
            data_devolucao = datetime.strptime(data["data_devolucao"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use o formato YYYY-MM-DD"}), 400

        
        emprestimo = userLivroBiblioteca(
            id=self.model.next_val(),  
            id_usuario=data["id_usuario"],
            id_livro=data["id_livro"],
            nome_user=data["nome_user"],
            titulo_livro=data["titulo_livro"],
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )

        
        self.model.criar_emprestimo(emprestimo)
        return jsonify({"message": "Empréstimo de livro criado com sucesso!"}), 201

    def atualizar_emprestimo(self, id):
        
        data = request.get_json()

       
        try:
            data_emprestimo = datetime.strptime(data["data_emprestimo"], "%Y-%m-%d")
            data_devolucao = datetime.strptime(data["data_devolucao"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use o formato YYYY-MM-DD"}), 400
        
        emprestimo = userLivroBiblioteca(
            id=id, 
            id_usuario=data["id_usuario"],
            id_livro=data["id_livro"],
            nome_user=data["nome_user"],
            titulo_livro=data["titulo_livro"],
            data_devolucao=data_devolucao,
            data_emprestimo=data_emprestimo
        )

        result = self.model.atualizar_emprestimo(emprestimo)
        if result:
            return jsonify({"message": "Empréstimo de livro atualizado com sucesso!"})
        else:
            return jsonify({"message": "Empréstimo de livro não encontrado!"}), 404

    def deletar_emprestimo(self, id):

        result = self.model.deletar_emprestimo(id)
        if result:
            return jsonify({"message": "Empréstimo de livro deletado com sucesso!"})
        else:
            return jsonify({"message": "Empréstimo de livro não encontrado!"}), 404
