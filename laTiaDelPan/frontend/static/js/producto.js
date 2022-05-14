$(document).ready(function() {
    var selected = [];
      var tabla= $('#tablaProducto').DataTable({
          pageLength: '25',
          destroy: true,
          autoWidth: false,
          columnDefs:[
              {targets:2,ordenable:true,width:'20%'},
              {targets:4,ordenable:false,width: '15%'},
            ],
          select: {
               style:    'os',
               selector: 'td:first-child'
           },
           order: [[ 0, 'asc' ]],

           "columns":[
            {"data":"nombreProducto"},
            {"data":"Categoria"},
            {"data":"Proveedor"},
            {"data":"stock"},
            {"data":"precioUnitario"},
            {"data":"estadoProducto"},
            {
                "data": null,
                "className": "button",
                "defaultContent": 
                "<button value='id' class='btn btn-success' data-toggle='modal' data-target='#editarCategoria'>Editar</button><button style='margin-left: 10px;' class='btn btn-primary'>Cambiar Estado</button"
            }
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