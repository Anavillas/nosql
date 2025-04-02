var API_URL = ""; // Defina a URL da API
var listaLivros = [];

function editarLivro(lid) {
  const livro = listaLivros.find(l => l.id === lid);
  if (!livro) {
    Swal.fire({
      icon: 'error',
      title: 'Erro na busca',
      text: "Livro com ID: " + lid + " não foi localizado!"
    });
    return;
  }

  // Preenche os campos do modal com os dados do livro
  $("#inputId").val(livro.id);
  $("#inputId").attr("disabled", true); // Impede alteração do ID
  $("#inputTitulo").val(livro.titulo);
  $("#inputAutor").val(livro.autor);
  $("#inputGenero").val(livro.genero);
  $("#inputAno").val(livro.ano);
  
  $('#staticBackdrop').modal('show');
}

function carregarLivros() {
  $.ajax({
    url: API_URL + "/livros",
    method: "GET",
    success: function(dados) {
      listaLivros = dados;
      const tbody = $("#tabelaLivros tbody");
      tbody.empty();
      dados.forEach((l) => {
        tbody.append(
          `<tr>
            <td>${l.id}</td>
            <td>${l.titulo}</td>
            <td>${l.autor}</td>
            <td>${l.genero}</td>
            <td>${l.ano}</td>
            <td>
              <button class="btn btn-warning btn-sm" onclick="editarLivro(${l.id})">Editar</button>
              <button class="btn btn-danger btn-sm" onclick="deletarLivro(${l.id})">Deletar</button>
            </td>
          </tr>`
        );
      });
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function criarLivro() {
  const livro = {
    id: parseInt($("#inputId").val()),
    titulo: $("#inputTitulo").val(),
    autor: $("#inputAutor").val(),
    genero: $("#inputGenero").val(),
    ano: $("#inputAno").val()
  };
  
  $.ajax({
    url: API_URL + "/livros",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(livro),
    success: function(res) {
      Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
      carregarLivros();
      $("#formLivro")[0].reset(); // Limpa o formulário
      $('#staticBackdrop').modal('hide');
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function IncluirLivro() {
  // Limpa os campos antes de abrir o modal
  $("#inputId").val(0); // Para inclusão, o ID é 0
  $("#inputId").attr("disabled", false); // Permite editar o ID
  $("#inputTitulo").val("");
  $("#inputAutor").val("");
  $("#inputGenero").val("");
  $("#inputAno").val("");
  $('#staticBackdrop').modal('show');
}

function gravarDados() {
  let id = $("#inputId").val();
  if (id == 0) {
    criarLivro();
  } else {
    atualizarLivro();
  }
}

function atualizarLivro() {
  const lid = parseInt($("#inputId").val());
  const dados = {
    titulo: $("#inputTitulo").val(),
    autor: $("#inputAutor").val(),
    genero: $("#inputGenero").val(),
    ano: $("#inputAno").val()
  };
  
  $.ajax({
    url: API_URL + "/livros/" + lid,
    method: "PUT",
    contentType: "application/json",
    data: JSON.stringify(dados),
    success: function(res) {
      Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
      carregarLivros();
      $("#formLivro")[0].reset(); // Limpa o formulário
      $('#staticBackdrop').modal('hide');
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function deletarLivro(lid) {
  Swal.fire({
    title: 'Confirmação de Exclusão',
    text: `Tem certeza que deseja excluir o livro de ID ${lid}?`,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Sim, EXCLUIR!',
    cancelButtonText: 'Não'
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        url: API_URL + "/livros/" + lid,
        method: "DELETE",
        success: function(res) {
          Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
          carregarLivros();
        },
        error: function(err) {
          console.error(err);
        }
      });
    }
  });
}

$(document).ready(function(){
  carregarLivros(); // Carrega a lista de livros na inicialização
});
