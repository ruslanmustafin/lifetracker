$().ready(function () {
    $('.datetimepicker').datetimepicker({
        format: 'Y.MM.DD'
    });
});

function weightScripts() {
    $().ready(function () {
        $('#weight-table').on('click', '.remove-weight-btn', function (e) {
            var weightId = $(this).data('weightId');
            e.preventDefault();
            //$(this).parent('td').fadeOut().remove();
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

            //console.log(data);
            /*$.ajax({
                headers: {"X-CSRFToken": "LqiD1lJ3PJy3V1zAo0jFUPfipon8EaxQNh1OGTnO9Wyvl57Lam3hEYNiNrigIGeE"},
                type: "DELETE",
                //dataType: "jsonp",
                url: '/api/weight/' + weightId + '/',
                success: function (data) {
                    $(this).parent('td').fadeOut().remove();
                    console.log(data);
                }
            });*/
        });
        diff = 0;
        weightBuff = chartData[0][2];
        $.each(chartData, function (index, value) {
            diff = value[2] - weightBuff;
            $('#weight-table').append(
                '<tr><td>' + value[1] + '</td><td>' + value[2] + '</td><td><a href="#" data-weight-id=' + value[0] + ' class="remove-weight-btn"><span class="glyphicon glyphicon-trash"></span></a></td><td>' + diff + '</td></tr>'
            );
            weightBuff = value[2];
        });

        $('#weight_table').DataTable({
            "sDom": '<"row view-filter"<"col-sm-12"<"pull-left"l><"pull-right"f><"clearfix">>>t<"row view-pager"<"col-sm-12"<"text-center"ip>>>',
            searching   :   false,
            lengthChange :  false,
            info        :   false
        });
    });
}