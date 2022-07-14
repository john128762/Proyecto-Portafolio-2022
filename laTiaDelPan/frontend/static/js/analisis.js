$(document).ready(function() {
    var selected = [];
      var tabla= $('#tablaAnalisis').DataTable({
          pageLength: '10',
          destroy: true,
          autoWidth: false,
          columnDefs:[
          ],
          select: {
               style:    'os',
               selector: 'td:first-child'
           },
           order: [[ 0, 'asc' ]],

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

$(document).ready(function() {
  var selected = [];
    var tabla= $('#tablaAnalisisF').DataTable({
        pageLength: '10',
        destroy: true,
        autoWidth: false,
        columnDefs:[
          ],
        select: {
             style:    'os',
             selector: 'td:first-child'
         },
         order: [[ 0, 'asc' ]],

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