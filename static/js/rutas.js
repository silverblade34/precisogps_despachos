
const abrirModal = (message, status) =>{
    if (status == "true"){
        swal ( " ¡Buen trabajo! " , message, "success")   ;
    }else{
        swal ( " ¡Ocurrio un error! " , message, "error")   ;
    }      
}