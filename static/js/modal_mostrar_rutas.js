const btnseditarRutas = document.querySelectorAll(".btn-preciso-editar");

btnseditarRutas.forEach(btnseditarRuta => {
    btnseditarRuta.addEventListener("click", function () {
        const codRuta = this.dataset.codRuta;
        mostrarModalCarga();
        fetch(`/buscar_ruta_smq?codruta=${codRuta}`, {
            method: "GET",
        })
            .then(response => {
                cerrarModalCarga();
                if (!response.ok) {
                    throw new Error("Error al buscar ruta");
                }
                return response.json();
            })
            .then(data => {
                console.log(data)
                const dataanterior = data
                Swal.fire({
                    title: "Editar ruta",
                    titleClass: 'editar-ruta-title',
                    html: `
                <form class="form-mostrar-modal-ruta">
                    <p class="form-label">CODIGO_RUTA</p>
                    <input type="text" id="cod_ruta" class = "form-control input-text" value="${data.CODIGO_RUTA}" disabled>
                    <p class="form-label">GISROU_NOMBRE</p>
                    <input type="text" id="name_ruta" class = "form-control input-text" value="${data.GISROU_NOMBRE}">
                    <p for="" class="form-label">GISROU_PUNTOS</p>
                    <textarea name="textarea-coordenadas" id="ruta_coordenadas" cols="50" rows="10">${data.GISROU_PUNTOS}</textarea>
                    <p class="form-label">RUC OTT</p>
                    <input type="text" id="ruc_ruta_ott" class = "form-control input-text" value="${data.RUC_OTT}" disabled>
                    <p class="form-label">RUC PROVEEDOR</p>
                    <input type="text" id="ruc_ruta_prov" class = "form-control input-text" value="${data.RUC_PROVEEDOR}" disabled>
                </form>
                `,
                    showCancelButton: true,
                    confirmButtonText: "Actualizar ruta",
                    preConfirm: function () {
                        const name_ruta = document.getElementById("name_ruta").value;
                        const ruta_coordenadas = document.getElementById("ruta_coordenadas").value;
                        return {
                            dataanterior: dataanterior,
                            data: {
                                SM_NOMBRE: name_ruta,
                                SM_COORDENADAS: ruta_coordenadas
                            }
                        };
                    }
                }).then(function (result) {
                    if (result.value) {
                        const data = result.value;
                        if (!data.data.SM_NOMBRE || !data.data.SM_COORDENADAS) {
                            Swal.fire("Error", "No puede dejar esos campos vacios", "error");
                            return;
                        }
                        // Envía los datos del formulario a una ruta POST en Flask
                        fetch("/actualizar_ruta_smq", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(data)
                        })
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error("Error al actualizar la ruta");
                                }
                                return response.json();
                            })
                            .then(data => {
                                Swal.fire("Actualizado", "La "+ data.SM_CODIGO_RUTA + " se ha actualizado" + "!", "success");
                            })
                            .catch(error => {
                                console.error(error);
                                Swal.fire("Error", data.MENSAJE, "error");
                            });
                    }
                });
            })
    });
})

function mostrarModalCarga() {
    Swal.fire({
        title: '<h3 class="modal-title">Cargando datos...</h3>',
        html: '<div class="lds-dual-ring"></div>',
        allowOutsideClick: false,
        showCancelButton: false,
        showConfirmButton: false
    });
}

function cerrarModalCarga() {
    Swal.close();
}