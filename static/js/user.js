var API_URL = ""; 
var listaUsers = [];

function editarUser(uid) {
  const User = listaUsers.find(u => u.id === uid);
  if (!User) {
    Swal.fire({
      icon: 'error',
      title: 'Erro na busca',
      text: "User com ID: " + uid + " não foi localizado!"
    });
    return;
  }

  
  $("#inputId").val(User.id);
  $("#inputId").attr("disabled", true);
  $("#inputNome").val(User.nome);
  $("#inputFone").val(User.fone);
  const modal = new bootstrap.Modal(document.getElementById('modalAdicionarUser'));
  modal.show();
}

function carregarUsers() {
    $.ajax({
      url: API_URL + "/users",
      method: "GET",
      success: function(dados) {
        listaUsers = dados;
        const tbody = $("#tabelaUsuarios tbody");
        tbody.empty(); 
        dados.forEach(u => {
          tbody.append(`
            <tr>
              <td>${u.id}</td>
              <td>${u.nome}</td>
              <td>${u.fone}</td>
              <td>
                <button class="btn btn-warning btn-sm" onclick="editarUser(${u.id})">Editar</button>
                <button class="btn btn-danger btn-sm" onclick="deletarUser(${u.id})">Deletar</button>
              </td>
            </tr>
          `);
        });
      },
      error: function(err) {
        console.error('Erro ao carregar usuários', err);
      }
    });
  }
  

function criarUser() {
  const user = {
    id: parseInt($("#inputId").val()),
    nome: $("#inputNome").val(),
    fone: $("#inputFone").val()
  };
  
  $.ajax({
    url: API_URL + "/users",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(user),
    success: function(res) {
      Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
      carregarUsers();
      $("#formUser")[0].reset(); // Limpa o formulário
      $('#staticBackdrop').modal('hide');
    },
    error: function(err) {
      console.error(err);
    }
  });
}

function IncluirUser() {
  
  $("#inputId").val(0); 
  $("#inputId").attr("disabled", false); 
  $("#inputNome").val("");
  $("#inputFone").val("");
  $('#staticBackdrop').modal('show');
}

function gravarDadosUser() {
  let id = $("#inputId").val();
  if (id == 0) {
    criarUser();
  } else {
    atualizarUser();
  }
}

function atualizarUser() {
    const uid = parseInt($("#inputId").val());
    const dados = {
      nome: $("#inputNome").val(),
      fone: $("#inputFone").val() 
    };
    
    $.ajax({
      url: API_URL + "/users/" + uid,
      method: "PUT",
      contentType: "application/json",
      data: JSON.stringify(dados),
      success: function(res) {
        Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
        carregarUsers();
        $("#formUser")[0].reset(); 
        $('#staticBackdrop').modal('hide');
      },
      error: function(err) {
        console.error(err);
      }
    });
  }
  

function deletarUser(uid) {
  Swal.fire({
    title: 'Confirmação de Exclusão',
    text: `Tem certeza que deseja excluir o User de ID ${uid}?`,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Sim, EXCLUIR!',
    cancelButtonText: 'Não'
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        url: API_URL + "/users/" + uid,
        method: "DELETE",
        success: function(res) {
          Swal.fire({ icon: 'success', title: 'Sucesso', text: res.mensagem });
          carregarUsers();
        },
        error: function(err) {
          console.error(err);
        }
      });
    }
  });
}

$(document).ready(function(){
  carregarUsers();
});
