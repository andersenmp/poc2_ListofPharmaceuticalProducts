$(document).ready(function() {

    /* Medicines Data Grid Starts Here */
    medicineDataDS = new kendo.data.DataSource({
        page: 1,
        pageSize: 10,
        serverPaging: true,
        serverSorting: true,
        serverFiltering: true,
        filterable: {
            mode: "row"
        },
        schema: {
    	data: "results",
    	total: "total",
		model: {
			id: "id",
            fields: {
            	id:{ type: "number" ,editable: false},
            	name: {type: "string",editable: false},
            	composition: {type: "string",editable: false}

            }
        }
    },
        transport:
        {
            read: {
                url: "GetMedicalList/",
                dataType: "json",
                data: { cache: false, nocache: Math.random(), csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
                type: 'POST'
            }
        }
    });


    var medicineDataVar = $('#medicinesDataGrid').kendoGrid({
		dataSource: medicineDataDS,
		columns: setMedicineGridFileds(),
		toolbar: getMedicinesGridToolbarConfig(),
		excel: {
		    allPages: true
		},
		pageable: {
			pageSize: 10,
			pageSizes: [10, 20, 50]
		},
		filterable: {
			mode: 'row'
		},
		resizable: true,
         height: 600,
	});

	$("#medicinesDataGrid").data("kendoGrid").bind("excelExport", function (e) {catchExportExcel(e, "excel");});


	function getMedicinesGridToolbarConfig() {
        var config = [] ;
        var createButton = { name: 'create', text: 'Create' };

        config.push({ name: 'excel'});

        config.push(createButton);

        return config;
    }

	function setMedicineGridFileds() {
        var fields = [
            {field: 'name', title: 'Name', filterable: {cell: {showOperators: false}}},
            {field: 'composition', title:'Composition', filterable: {extra: false, cell: {showOperators: false}}}
        ]

        return fields;
    }


});
