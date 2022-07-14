$(document).ready(function() {
  var selected = [];
    var tabla= $('#tablaBoletas').DataTable({
        pageLength: '10',
        destroy: true,
        autoWidth: false,
        columnDefs:[
            {"targets":1,"ordenable":true,"width":'0%', "searchable": true },
            {"targets":[2,3,4],"ordenable":true,"width":'20%', "searchable": false },
          ],
        select: {
             style:    'os',
             selector: 'td:first-child'
         },
         order:[[3, 'desc'], [0, 'asc']],

         "columns":[
          {"data":"numBoleta"},
          {"data":"vendedor"},
          {"data":"total"},
          {"data":"estado"},
        ],

        language : {
           paginate: {
                 first: " |< ",
                 previous: "Ant.",
                 next: "Sig.",
                 last: " >| "
             },
          emptyTable:          "No hay datos disponibles en la tabla.",
          info:               "Del _START_ al _END_ de _TOTAL_",
          infoEmpty:       "Mostrando 0 registros de un total de 0.",
          infoFiltered:        "(filtrados de un total de MAX registros)",
          infoPostFix:         "(actualizados)",
          lengthMenu:          "Mostrar _MENU_ registros",
          loadingRecords:       "Cargando...",
          searchPlaceholder:    "Buscar ",
          zeroRecords:         "No se han encontrado coincidencias.",
          search:             "Buscar:" ,
          processing: "Procesando la información",
          select: {
          rows: "%d Registros Seleccionados"
             }
        },
     } );
} );