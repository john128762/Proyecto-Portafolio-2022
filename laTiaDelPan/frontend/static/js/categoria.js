
$(document).ready(function() {
    var selected = [];
      var tabla= $('#tablaCategoria').DataTable({
          pageLength: '25',
          destroy: true,
          autoWidth: false,
          columnDefs:[
              {targets:2,ordenable:true,width:'20%'},
              {targets:3,ordenable:false,width: '32%'},
            ],
          select: {
               style:    'os',
               selector: 'td:first-child'
           },
           order: [[ 0, 'asc' ]],

           "columns":[
            {"data":"nombreCategoria"},
            {"data":"descripcionCategoria"},
            {"data":"estadoCategoria"},
            {
                "data": null,
                "className": "button",
                "defaultContent": 
                "<button value='id' style='margin-left: 10px;' class='btn btn-success' data-toggle='modal' data-target='#EditarCategoria'>Editar</button><button value='id' style='margin-left: 10px;' class='btn btn-danger' data-toggle='modal' data-target='#EliminarCategoria'>Eliminar</button><button style='margin-left: 10px;' class='btn btn-primary'>Cambiar Estado</button"
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