var API_URL = ""; // Defina a URL da API
var listaUsers = [];

function formatarTeleFone(Fone) {
    if (!Fone) return "TeleFone inválido";  // Verificação extra
    let digits = Fone.replace(/\D/g, "");
    
    if (digits.length === 10) {
      const ddd = digits.slice(0, 2);
      const parte1 = digits.slice(2, 6);
      const parte2 = digits.slice(6);
      return `(${ddd}) ${parte1}-${parte2}`;
    } else if (digits.length === 11) {
      const ddd = digits.slice(0, 2);
      const parte1 = digits.slice(2, 7);
      const parte2 = digits.slice(7);
      return `(${ddd}) ${parte1}-${parte2}`;
    } else {
      return Fone + " [Fone inválido]";
    }
}

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

  // Preenche os campos do modal com os dados do User
  $("#inputId").val(User.id);
  $("#inputId").attr("disabled", true); // Impede alteração do ID
  $("#inputNome").val(User.nome);
  $("#inputFone").val(User.fone);
  $('#staticBackdrop').modal('show');
}

function carregarUsers() {
    $.ajax({
      url: API_URL + "/Users",
      method: "GET",
      success: function(res) {
        let tabelaUsuarios = $('#tabelaUsuarios tbody');
        tabelaUsuarios.empty(); // Limpa a tabela antes de adicionar novos dados
        res.forEach(user => {
          tabelaUsuarios.append(`
            <tr>
              <td>${user.id}</td>
              <td>${user.nome}</td>
              <td>${user.fone}</td>
              <td>
                <button class="btn btn-info" onclick="editarUser(${user.id})">Editar</button>
                <button class="btn btn-danger" onclick="deletarUser(${user.id})">Deletar</button>
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
  const User = {
    id: parseInt($("#inputId").val()),
    nome: $("#inputNome").val(),
    fone: $("#inputFone").val()
  };
  
  $.ajax({
    url: API_URL + "/Users",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(User),
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
  // Limpa os campos antes de abrir o modal
  $("#inputId").val(0); // Para inclusão, o ID é 0
  $("#inputId").attr("disabled", false); // Permite editar o ID
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
      fone: $("#inputFone").val(), // Corrigido o ID para 'inputFone' com "F" maiúsculo
    };
    
    $.ajax({
      url: API_URL + "/Users/" + uid,
      method: "PUT",
      contentType: "application/json",
      data: JSON.stringify(dados),
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
        url: API_URL + "/Users/" + uid,
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
  carregarUsers(); // Carrega a lista de Users na inicialização
});
