from flask import jsonify, request
from datetime import datetime
from MODEL.userLivroBiblioteca import userLivroBiblioteca, userLivroModel

class UserLivroBibliotecaController:
    """Controlador para manipular empréstimos de livros na biblioteca."""

    def __init__(self):
        self.model = userLivroModel()

    def contar_emprestimos(self):
        """Contar o total de empréstimos de livros."""
        total = self.model.contar_emprestimos()
        return jsonify({'total': total})

    def listar_emprestimos(self):
        """Listar todos os empréstimos de livros."""
        emprestimos = self.model.listar_emprestimos()
        return jsonify(emprestimos)

    def criar_emprestimo(self):
        """Criar um novo empréstimo de livro."""
        data = request.get_json()  # Pegando os dados do corpo da requisição
        
        # Validação das datas
        try:
            data_emprestimo = datetime.strptime(data["data_emprestimo"], "%Y-%m-%d")
            data_devolucao = datetime.strptime(data["data_devolucao"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use o formato YYYY-MM-DD"}), 400

        # Criando a instância do empréstimo
        emprestimo = userLivroBiblioteca(
            id=self.model.next_val(),  # Usa o próximo valor de ID gerado pelo MongoDB
            id_usuario=data["id_usuario"],
            id_livro=data["id_livro"],
            nome_user=data["nome_user"],
            titulo_livro=data["titulo_livro"],
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )

        # Chama o método para salvar no banco
        self.model.criar_emprestimo(emprestimo)
        return jsonify({"message": "Empréstimo de livro criado com sucesso!"}), 201

    def atualizar_emprestimo(self, id):
        """Atualizar os dados de um empréstimo de livro."""
        data = request.get_json()

        # Validação das datas
        try:
            data_emprestimo = datetime.strptime(data["data_emprestimo"], "%Y-%m-%d")
            data_devolucao = datetime.strptime(data["data_devolucao"], "%Y-%m-%d")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use o formato YYYY-MM-DD"}), 400
        
        emprestimo = userLivroBiblioteca(
            id=id,  # Usando "id" como identificador
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
        """Deletar um empréstimo de livro."""
        result = self.model.deletar_emprestimo(id)
        if result:
            return jsonify({"message": "Empréstimo de livro deletado com sucesso!"})
        else:
            return jsonify({"message": "Empréstimo de livro não encontrado!"}), 404
