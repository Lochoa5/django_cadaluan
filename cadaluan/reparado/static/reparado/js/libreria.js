function confirmar_eliminar(ruta){
    if(confirm("Está seguro?")){
        location.href = ruta;
    }
    else{
        alert("Fiuu, te salvaste...")
    }
}