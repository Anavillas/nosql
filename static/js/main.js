$(document).ready(function() {
  // Ao clicar em "Biblioteca" no menu, carregamos a página correspondente
  $("#linkBiblioteca").click(function(e) {
      e.preventDefault();
      // Verifica se a div já contém conteúdo
      if ($("#divPrincipal").children().length === 0) {
          $("#divPrincipal").load("/view/livros", function() {
              // Após carregar o HTML, carregamos o script do CRUD
              $.getScript("/static/js/livros.js")
                  .done(function() {
                      console.log("Script de livros carregado com sucesso.");
                      // Inicializa os eventos e carrega a lista de livros
                  })
                  .fail(function() {
                      console.error("Não foi possível carregar livros.js");
                  });
          });
      }
  });
});
