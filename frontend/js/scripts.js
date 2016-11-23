$().ready(function () {
    $('.datetimepicker').datetimepicker({
        format: 'Y.MM.DD'
    });
});

function weightScripts() {
    $().ready(function () {
        // build table
        diff = 0;
        weightBuff = chartData[0][2];
        $.each(chartData, function (index, value) {
            diff = value[2] - weightBuff;
            $('#weight-table').append(
                '<tr><td>' + value[1] + '</td><td>' + value[2] + '</td><td><a href="#" data-weight-id=' + value[0] + ' class="remove-weight-btn"><span class="glyphicon glyphicon-trash"></span></a></td><td>' + diff + '</td></tr>'
            );
            weightBuff = value[2];
            console.log('table edit')
        });

        var $dataTable = $('#weight_table').DataTable({
            "sDom": '<"row view-filter"<"col-sm-12"<"pull-left"l><"pull-right"f><"clearfix">>>t<"row view-pager"<"col-sm-12"<"text-center"ip>>>',
            searching: false,
            lengthChange: false,
            info: false
        });

        // refresh table to reflect new data
        $dataTable.draw();

        // remove data entrance
        $('#weight_table').on('click', '.remove-weight-btn', function (e) {
            e.preventDefault();
            // weigh tmodel id
            var weightId = $(this).data('weightId');
            var $row = $(this).parents('tr');
            $.ajax({
                // REST interaction
                headers: {"X-CSRFToken": $.cookie('csrftoken')},
                type: "DELETE",
                //dataType: "jsonp",
                url: '/api/weight/' + weightId + '/',
                success: function (data) {
                    // remove table row
                    $row.stop(true,true).fadeOut(function () {
                        $dataTable.row($row).remove().draw();
                    });
                    // update graph
                    for (var i = 0; i < chartData.length; i++) {
                        if (chartData[i][0] == weightId) {
                            console.log(chartData[i]);
                            chartData.splice(i, 1);
                            graphData.labels.splice(i, 1);
                            graphData.weightData.splice(i, 1);
                            myChart.update();
                            break;
                        }
                    }
                    console.log(data);
                }
            });
        });
    });
}