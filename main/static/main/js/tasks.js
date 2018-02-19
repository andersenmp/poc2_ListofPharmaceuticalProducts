
/**
 * This file is required if tasks are used in the information system
 */



var popupAddTask = new Popup({
  id: 'popup-add-task',
  isForm: true,
  title: 'Add new task',
  content: 
    '<div class="form-group"><label for="task-subject">Subject</label>' + 
    '<input type="text" id="task-subject" class="form-control"></div>' +
    '<div class="form-group"><label for="task-due-date">Due date</label>' +
    '<input type="date" id="task-due-date" class="form-control"></div>' +
    '<div class="form-group"><label for="task-body">Description</label>' + 
    '<textarea id="task-body" class="form-control"></textarea></div>' + 
    '<div class="form-group"><label for="task-upload">Upload File</label>' +
    '<input type="file" id="task-upload"></div>',
  buttons: [{
    label: 'Add',
    type: 'success',
    glyph: 'ok',
    click: "alert('todo: save task'); $('#popup-add-task').modal('hide');"
  },
  {
    label: 'Cancel',
    type: 'default',
    glyph: 'remove',
    click: "$('#popup-add-task').modal('hide');"
  }]
});

popupAddTask.add();

$("#task-upload").kendoUpload();


// date picker
if (!isMobile) {
  $('#task-due-date').removeClass('form-control').kendoDatePicker({
    format: 'dd/MM/yyyy',
  });
}

var currentDate = new Date();
var tasksSD = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate(), 0, 0, 0, 0);
var tasksED = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate(), 23, 59, 59, 999);

var tasksDS = new kendo.data.DataSource({
    page: 1,
    pageSize: 10,
    serverPaging: false,
        serverSorting: false,
        serverFiltering: false,
        schema: {
          data: "results",
          total: "total",
          model: {
                id: "hrp_task_id",
                fields: {
                  hrp_task_id: { 
                    type: "number" 
                  },
                  from_perid: { 
                    type: "number" 
                  },
                  to_perid: {
                    type: "number"
                  },
                  subject: {
                    type: "string"
                  },
                  task_body: {
                    type: "string"
                  },
                  due_date: {
                    type: "string"
                  },
                  due_date_epoch: {
                    type: "number"
                  },
                  diff_days: {
                    type: "number" 
                  },
                  completed: {
                    type: "number"
                  },
                  hrp_task_attachment_id: {
                    type: "number"
                  },
                  file_name: {
                    type: "string"
                  }
                }
          }
        },
    transport: {
      read: {
        url: "js/tasks.json",
        dataType: "json",
        type: 'POST',
        data: {
          fuseaction: 'home.tasksJSON',
          tasksStartDate: tasksSD,
          tasksEndDate: tasksED,
          // tasksStartDate: $.formatDateTime('yy-mm-dd hh:ii:ss', tasksSD),
          // tasksEndDate : $.formatDateTime('yy-mm-dd hh:ii:ss', tasksED),
          completed: 0
        }
      }
    }
  });


$('#tasks-grid').kendoGrid({
    dataSource: tasksDS,
    columns: [
      {
        title: '',
        template: function(dataItem) {
          var returnStr = "<input type=\"checkbox\" name=\"completeTask\" id=\"check_"+dataItem.hrp_task_id+"\" data-task-id=\""+dataItem.hrp_task_id+"\" class=\"nolabel\" value=\""+dataItem.hrp_task_id+"\" "
          if (dataItem.completed == 1) {
            returnStr += "checked='checked' ";
          }
          returnStr += " />";
            return returnStr;
        },
        attributes: {
          style: 'text-align:center'
        },
        headerAttributes: {
          style: 'text-align:center'
        },
        width: "5%"
      },
      {
        title: getString('labels.tasks.subject'),
        field: 'subject',
        template: function(dataItem) {
          return '<a href="javascript:void(0)" onclick="expandTaskRow(\''+dataItem.uid+'\')">'+dataItem.subject+'</a>';
          /*console.log(arguments);
          console.log(dataItem.parent());
          console.log($('.k-master-row[data-uid="'+dataItem.uid+'"]'));
          $('#tasks-grid').data('kendoGrid').expandRow('.k-master-row[data-uid="'+dataItem.uid+'"]');*/
        },
        attributes: {
          style: 'text-align:left'
        },
        headerAttributes: {
          style: 'text-align:left'
        },
        width: "45%"
      },
      {
        title: getString('labels.tasks.duedate'),
        field: 'due_date_epoch',
        template: function(dataItem) {
          return dataItem.due_date;
        },
        attributes: {
          style: 'text-align:center'
        },
        headerAttributes: {
          style: 'text-align:center'
        },
        width: "20%"
      },
      {
        title: getString('labels.tasks.daysleft'),
        field: 'diff_days',
        attributes: {
          style: 'text-align:center'
        },
        headerAttributes: {
          style: 'text-align:center'
        },
        width: "10%"
      },
      {
        title: getString('labels.common.action'),
        template: function(dataItem) {
          returnStr = '<button type="button" onclick="editTask('+dataItem.hrp_task_id+')" class="btn btn-primary btn-xs no-icon btn-no-min-width" style="padding:0px 10px">';
          returnStr += getString('buttons.common.edit');
          returnStr += '</button>';
          returnStr += '<button type="button" onclick="deleteTask('+dataItem.hrp_task_id+')" class="btn btn-primary btn-xs no-icon btn-no-min-width" style="padding:0px 10px">';
          returnStr += getString('buttons.common.delete');
          returnStr += '</button>';
          return returnStr;
        },
        attributes: {
          style: 'text-align:center; padding-top: 7px;'
        },
        headerAttributes: {
          style: 'text-align:center'
        },
        width: "20%"
      }
    ],
    sortable: true,
    dataBound: onDataBound,
    pageable: {
      pageSize: 10,
      pageSizes: false
    },
    detailTemplate: function(dataItem) {
      var returnStr = '<div class="tasks-details-container">';
      returnStr += '<div class="tasks-details-title">'+getString('labels.tasks.subject')+':</div><div class="tasks-details-text">'+dataItem.subject+'</div>';
      returnStr += '<div class="tasks-details-title">'+getString('labels.tasks.duedate')+':</div><div class="tasks-details-text">'+dataItem.due_date+'</div>';
      returnStr += '<div class="tasks-details-title">'+getString('labels.tasks.body')+':</div><div class="tasks-details-text">'+dataItem.task_body+'</div>';
      if($.trim(dataItem.hrp_task_attachment_id) != '') {
        returnStr += '<div class="tasks-details-title">'+getString('labels.tasks.attachments')+':</div><div class="tasks-details-text"><a href="javascript:void(0)" onclick="downloadTaskAttachment('+dataItem.hrp_task_attachment_id+')" class="task-attachment-link">'+dataItem.file_name+'</a></div>';
      };
      returnStr += '</div>';
      return returnStr;
      
    },
    detailExpand: function(e){
      var tooltip = e.masterRow.find('td.k-hierarchy-cell').data("kendoTooltip");
      tooltip.destroy();
      e.masterRow.find('td.k-hierarchy-cell').kendoTooltip({
        content: getString('labels.tasks.tooltiphide'),
        position: 'left',
        autoHide: true
      }).data("kendoTooltip").show();
      
    },
    detailCollapse: function(e) {
      var tooltip = e.masterRow.find('td.k-hierarchy-cell').data("kendoTooltip");
      tooltip.destroy();
      e.masterRow.find('td.k-hierarchy-cell').kendoTooltip({
        content: getString('labels.tasks.tooltipshow'),
        position: 'left',
        autoHide: true
      }).data("kendoTooltip").show();
    }
  });



function onDataBound(arg) {
  $('#tasks-grid td.k-hierarchy-cell').each(function(idx, elem){
    $(this).kendoTooltip({
      content: getString('labels.tasks.tooltipshow'),
      position: 'left',
      autoHide: true
    })
  });
  $('td[role="gridcell"] input[type="checkbox"]').each(function(){
    var checkbox = $(this);
    checkbox.addClass('hide').after('<label for="' + checkbox.attr('id') + '" class="check' + (checkbox.hasClass('nolabel') ? ' nolabel' : '' )+ '"></label>');
    checkbox.off('click').on('click', function(){
      var taskCompleted = 0;
      if($(this).is(':checked')) {
        taskCompleted = 1;
      }
      $.ajax({
        url: 'index.cfm',
        type: 'POST', 
        dataType: 'json',
        data: {
          fuseaction: 'home.editTask',
          editHrpTaskID: $(this).attr('data-task-id'),
          completed: taskCompleted
        },
        success: function(data) {
          if(!data.ERROR) {
            toastr.success(getString('messages.tasks.successave'), getString('labels.common.success'));
              } else { 
                toastr.error(data.MESSAGE, getString('labels.common.error'));
              }
            },
        complete: function(data) {
          updateTasksBadges();
          $('#tasks-grid').data('kendoGrid').dataSource.read();
          $("#tasks-grid").data("kendoGrid").refresh();
            }
      });
    })
  });
  kendo.ui.progress($('.tasks-dropdown'), false);
};



$('#tasks-tabs').kendoTabStrip();


var tasks = $('#tasks');
var showTasksButton = $('#show-tasks');
showTasksButton.on('click', function(e){

  e.stopPropagation();
  e.preventDefault();
  

  if (!showTasksButton.hasClass('open')) {
    showTasksButton.addClass('open');
    tasks.fadeIn(150);
  }

  // close tasks popover
  else {
    closeTasksPopover();
  }
});


function closeTasksPopover() {
  showTasksButton.removeClass('open');
  tasks.fadeOut(150);
}



// hide tasks popover when clicking outside of it
$(document).on('click', function() {
  closeTasksPopover();
})

// but don't hide it when clicking in the tasks popover ...
tasks.on('click', function(e) {
  e.stopPropagation();
})

// ... or the "add task" popover
$('#popup-add-task').on('click', function(e) {
  e.stopPropagation();
})