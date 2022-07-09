$(document).ready(function() {
    var selected = [];
      var tabla= $('#tablaProducto').DataTable({
          pageLength: '25',
          destroy: true,
          autoWidth: false,
          columnDefs:[
              {targets:0,ordenable:true,width:'20%'},
              {targets:7,ordenable:false,width: '15%'},
            ],
          select: {
               style:    'os',
               selector: 'td:first-child'
           },
           order: [[ 0, 'asc' ]],

           "columns":[
            {"data":"codigo"},
            {"data":"nombreProducto"},
            {"data":"Categoria"},
            {"data":"Proveedor"},
            {"data":"stock"},
            {"data":"precioUnitario"},
            {"data":"estadoProducto"},
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