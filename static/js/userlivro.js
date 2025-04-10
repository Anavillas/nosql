var API_URL = "http://localhost:5000"; // Defina a URL da API conforme necessário
var listaLivros = [];
var listaUsuarios = [];
var listaEmprestimos = [];

function editarEmprestimo(eid) {
  const emprestimo = listaEmprestimos.find(e => e.id === eid);
  if (!emprestimo) {
    Swal.fire({
      icon: 'error',
      title: 'Erro na busca',
      text: "Empréstimo não encontrado com ID: " + eid
    });
    return;
  }

  // Preenche os campos do modal com os dados do empréstimo
  $("#inputIdLivro").val(emprestimo.id_livro);
  $("#inputIdLivro").attr("disabled", true);  // Desabilita o campo ID do livro
  $("#inputIdUsuario").val(emprestimo.id_usuario);
  
  // Carrega automaticamente as informações do livro e usuário
  carregarInfoLivro(emprestimo.id_livro);
  carregarInfoUsuario(emprestimo.id_usuario);

  $("#inputDataEmprestimo").val(emprestimo.data_emprestimo);
  $("#inputDataDevolucao").val(emprestimo.data_devolucao);
  
  $('#staticBackdrop').modal('show');
}

// Função para carregar as informações do livro a partir do ID
function carregarInfoLivro(lid) {
  $.ajax({
    url: API_URL + "/livros/" + lid,  // Rota para buscar livro por ID
    method: "GET",
    success: function(livro) {
      $("#inputIdTitulo").val(livro.titulo);  // Preenche o campo título do livro
    },
    error: function(err) {
      console.error('Erro ao carregar livro', err);
    }
  });
}

// Função para carregar as informações do usuário a partir do ID
function carregarInfoUsuario(uid) {
  $.ajax({
    url: API_URL + "/users/" + uid,  // Rota para buscar usuário por ID
    method: "GET",
    success: function(usuario) {
      $("#inputIdNomeUsuario").val(usuario.nome);  // Preenche o campo nome do usuário
    },
    error: function(err) {
      console.error('Erro ao carregar usuário', err);
    }
  });
}

function carregarEmprestimos() {
  $.ajax({
    url: API_URL + "/emprestimos-livros",  // URL para buscar os empréstimos
    method: "GET",
    success: function(dados) {
      const tbody = $("#tabelaEmprestimos tbody");
      tbody.empty();  // Limpa a tabela antes de adicionar novos dados

      // Itera sobre os dados dos empréstimos
      dados.forEach((emprestimo) => {
        // Encontrar o livro e o usuário a partir dos IDs
        const livro = listaLivros.find(l => l.id === emprestimo.id_livro);
        const usuario = listaUsuarios.find(u => u.id === emprestimo.id_usuario);
        
        // Preenche a tabela com os dados dos empréstimos
        tbody.append(`
          <tr>
            <td>${livro ? livro.id : 'ID não encontrado'}</td>
            <td>${livro ? livro.titulo : 'Livro não encontrado'}</td>
            <td>${usuario ? usuario.id : 'ID não encontrado'}</td>
            <td>${usuario ? usuario.usuario_nome : 'Usuário não encontrado'}</td>
            <td>${emprestimo.data_emprestimo}</td>
            <td>${emprestimo.data_devolucao}</td>
            <td>
              <button class="btn btn-warning btn-sm" onclick="editarEmprestimo(${emprestimo.id})">Editar</button>
              <button class="btn btn-danger btn-sm" onclick="deletarEmprestimo(${emprestimo.id})">Deletar</button>
            </td>
          </tr>
        `);
      });
    },
    error: function(err) {
      console.error('Erro ao carregar os empréstimos', err);
    }
  });
}

function carregarLivros() {
  $.ajax({
    url: API_URL + "/livros",  // Rota para listar os livros
    method: "GET",
    success: function(dados) {
      listaLivros = dados;
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function carregarUsuarios() {
  $.ajax({
    url: API_URL + "/users",  // Rota para listar os usuários
    method: "GET",
    success: function(dados) {
      listaUsuarios = dados;
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function criarEmprestimo() {
  const emprestimo = {
    id_usuario: parseInt($("#inputIdUsuario").val()),
    id_livro: parseInt($("#inputIdLivro").val()),
    data_emprestimo: $("#inputDataEmprestimo").val(),
    data_devolucao: $("#inputDataDevolucao").val()
  };
  
  $.ajax({
    url: API_URL + "/emprestimos-livros",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(emprestimo),
    success: function(res) {
      Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
      carregarEmprestimos();  // Atualiza a tabela de empréstimos
      $("#formEmprestimo")[0].reset(); // Limpa o formulário
      $('#staticBackdrop').modal('hide');
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function IncluirEmprestimo() {
  // Limpa os campos antes de abrir o modal
  $("#inputIdLivro").val(0); // Para inclusão, o ID do livro é 0
  $("#inputIdUsuario").val("");
  $("#inputIdNomeUsuario").val(""); // Corrigido a vírgula
  $("#inputIdTitulo").val(""); // Corrigido a vírgula
  $("#inputDataEmprestimo").val("");
  $("#inputDataDevolucao").val("");
  $('#staticBackdrop').modal('show');
}

function gravarDadosEmprestimo() {
  let eid = $("#inputIdLivro").val();
  if (eid == 0) {
    criarEmprestimo();
  } else {
    atualizarEmprestimo();
  }
}

function atualizarEmprestimo() {
  const eid = parseInt($("#inputIdLivro").val());
  const dados = {
    id_usuario: parseInt($("#inputIdUsuario").val()),
    id_livro: parseInt($("#inputIdLivro").val()),
    data_emprestimo: $("#inputDataEmprestimo").val(),
    data_devolucao: $("#inputDataDevolucao").val()
  };
  
  $.ajax({
    url: API_URL + "/emprestimos-livros/" + eid,  // Usando o ID do empréstimo para atualização
    method: "PUT",
    contentType: "application/json",
    data: JSON.stringify(dados),
    success: function(res) {
      Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
      carregarEmprestimos();  // Atualiza a tabela de empréstimos
      $("#formEmprestimo")[0].reset(); // Limpa o formulário
      $('#staticBackdrop').modal('hide');
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function deletarEmprestimo(eid) {
  Swal.fire({
    title: 'Confirmação de Exclusão',
    text: `Tem certeza que deseja excluir o empréstimo do Livro ID ${eid}?`,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Sim, EXCLUIR!',
    cancelButtonText: 'Não'
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        url: API_URL + "/emprestimos-livros/" + eid,
        method: "DELETE",
        success: function(res) {
          Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
          carregarEmprestimos();  
        },
        error: function(err) {
          console.error(err);
        }
      });
    }
  });
}

$(document).ready(function(){
  carregarLivros();  
  carregarUsuarios();  
  carregarEmprestimos();  
});
