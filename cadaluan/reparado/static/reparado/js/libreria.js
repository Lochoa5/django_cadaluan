function categorias_editar(ruta) {
    $.ajax({
        method: "GET",
        url: ruta,
    })
    .done(function(respuesta) {
        $("#editarModal").html(respuesta);
        $('#editarModal').modal('show');
    })
    .fail(function() {
        console.error("La respuesta del servidor no es válida.");
        alert("Ocurrió un error al procesar la respuesta del servidor.");
    });
}


/*
function categorias_editar(ruta) {
    r = $("#editarModal");

    $.ajax({
        method: "GET",
        url: ruta,
    })
    .done(function (respuesta) {
        r.html(respuesta);
        $('#editarModal').modal('show');

        // Agregar manejador de eventos para el formulario
        $('#formEditarCategoria').submit(function (event) {
            event.preventDefault();

            $.ajax({
                method: "POST",
                url: ruta,
                data: $('#formEditarCategoria').serialize(),
            })
            .done(function (response) {
                if (response.status === 'success') {
                    // Cerrar modal o realizar acciones adicionales
                    $('#editarModal').modal('hide');
                    // Puedes recargar la página o actualizar solo la tabla de categorías
                }
            })
            .fail(function () {
                alert("error");
            });
        });
    })
    .fail(function () {
        alert("error");
    });
}
*/