$(document).ready(function() {
    function carregarConteudos() {
        $("#divUsuarios").load("/view/user", function(response, status, xhr) {
            if (status === "success") {
                console.log("Conteúdo de Usuários carregado com sucesso.");
            } else {
                console.error("Erro ao carregar Usuários: " + xhr.status);
            }
        });

        $("#divLivros").load("/view/livros", function(response, status, xhr) {
            if (status === "success") {
                console.log("Conteúdo de Livros carregado com sucesso.");
            } else {
                console.error("Erro ao carregar Livros: " + xhr.status);
            }
        });

        $("#divLivros").load("/view/livros", function(response, status, xhr) {
            if (status === "success") {
                console.log("Conteúdo de Livros carregado com sucesso.");
            } else {
                console.error("Erro ao carregar Livros: " + xhr.status);
            }
        });

        $("#divUserLivro").load("/view/userlivro", function(response, status, xhr) {
            if (status === "success") {
                console.log("Conteúdo de Livros Emprestados carregado com sucesso.");
            } else {
                console.error("Erro ao carregar Livros Emprestados: " + xhr.status);
            }
        });

        contarTotal();
    }
    function contarTotal(){
        $.getJSON("/contar-livros", function (data) {
            $("#totalLivros").text(data.total);
        }).fail(function () {
            console.error("Erro ao contar livros.");
        });

        $.getJSON("/contar-users", function (data) {
            $("#totalUsers").text(data.total);
        }).fail(function () {
            console.error("Erro ao contar usuários.");
        });
    }
    carregarConteudos();
});