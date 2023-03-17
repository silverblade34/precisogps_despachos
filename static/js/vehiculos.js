$(document).ready(function() {
    // Agrega la opción de exportar a Excel y PDF
    $('#tabla-vehiculos').DataTable({
        dom: 'Bfrtip',
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json"
        },
        stripeClasses: ['stripe1', 'stripe2'],
        buttons: [
            {
                extend: 'excelHtml5',
                className: 'btn-exportar'
            },
            {
                extend: 'csvHtml5',
                className: 'btn-exportar'
            },
            {
                extend: 'pdfHtml5',
                className: 'btn-exportar'
            }
        ]
    });
});

