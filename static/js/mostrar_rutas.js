
const abrirModal = (message, status) => {
    if (status == "true") {
        swal(" ¡Buen trabajo! ", message, "success");
    } else {
        swal(" ¡Ocurrio un error! ", message, "error");
    }
}

const btnCargarRuta = document.querySelectorAll(".btn-cargar-ruta");

btnCargarRuta.forEach(btnCargarRut => {
    btnCargarRut.addEventListener("click", function () {
        // Mostrar el modal de SweetAlert con el mensaje de carga
        const loadingModal = Swal.fire({
            html: `
                <p class="text-lg font-bold text-gray-500 text-center">Se está construyendo el payload...</p>
            `,
            showCancelButton: false,
            showConfirmButton: false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
        });

        const codigoRuta = this.dataset.codRuta;
        console.log("----CODIGO RUTA----")
        console.log(codigoRuta)
        fetch(`/data_ruta_nimbus`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    "rutacodigo": codigoRuta
                }
            )
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al buscar data de la cuenta");
            }
            return response.json();
        })
        .then(data => {
            // Convertir los datos en formato JSON a una cadena con formato JSON
            const jsonData = JSON.stringify(data.data, null, 2);

            // Cerrar el modal de carga
            loadingModal.close();

            // Mostrar el modal de SweetAlert con los datos en formato JSON
            Swal.fire({
                html: `
                <div>
                    <p class="text-lg font-bold text-gray-500 text-center pb-5">Código de Ruta: ${data.codruta}</p>
                    <div class="w-full max-h-[40rem] min-h-[20rem] bg-gray-800 text-white p-3 overflow-y-auto rounded-lg">
                        <pre class="h-full w-full whitespace-pre-wrap text-xs">${jsonData}</pre>
                    </div>
                </div>
                `,
                showCancelButton: true,
                cancelButtonColor: '#9b9b9b',
                cancelButtonText: 'Cancelar',
                confirmButtonText: 'Cargar'
            }).then((result) => {
                // Si se hace clic en el botón "Cargar", enviar los datos al backend
                if (result.isConfirmed) {
                    // Realizar la consulta al backend utilizando el método POST y enviando los datos en el body
                    fetch('/enviar_ruta_smq', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data.data)
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error("Error al cargar los datos al backend");
                        }
                        // Mostrar un mensaje de éxito si todo salió bien
                        Swal.fire({
                            icon: 'success',
                            title: 'Datos cargados correctamente',
                            text: 'Los datos se han cargado correctamente a SMQ',
                        });
                    })
                    .catch(error => {
                        // Mostrar un mensaje de error si ocurrió un problema al cargar los datos al backend
                        Swal.fire({
                            icon: 'error',
                            title: 'Error',
                            text: error.message,
                        });
                    });
                }
            });
        })
        .catch(error => {
            // Cerrar el modal de carga en caso de error
            loadingModal.close();

            // En caso de error, mostrar un mensaje de error con SweetAlert
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: error.message,
            });
        });
    });
});
