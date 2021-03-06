$(document).ready(function() {
    var selected = [];
      var tabla= $('#tablaFactura').DataTable({
        "dom": 'rtip<"clear">',
        pageLength: '25',
        destroy: true,
        autoWidth: false,
        columnDefs:[
            {targets:2,ordenable:true,width:'20%'},
            {targets:4,ordenable:false,width: '2%'},
          ],
        select: {
             style:    'os',
             selector: 'td:first-child'
         },
         order: [[ 0, 'asc' ]],

         "columns":[
          {"data":"nombreProducto"},
          {"data":"categoriaProducto"},
          {"data":"cantidad"},
          {"data":"valor"},
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
