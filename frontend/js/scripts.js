$().ready(function () {

});

function weightScripts() {
    $().ready(function () {
        $('#weight-table').on('click', '.remove-weight-btn', function (e) {
            var weightId = $(this).data('weightId');
            e.preventDefault();
            $.ajax({
                type: "DELETE",
                //dataType: "jsonp",
                url: '/api/weight/' + weightId,
                success: function (data) {
                    $(this).parents('tr').fadeOut().remove();
                    console.log(data);
                }
            });
        });
        diff = 0;
        weightBuff = chartData[0][2];
        $.each(chartData, function (index, value) {
            diff = value[2] - weightBuff;
            $('#weight-table').append(
                '<tr><td>' + value[1] + '</td><td>' + value[2] + '</td><td><a href="#" data-weight-id=' + value[0] + ' class="remove-weight-btn"><span class="glyphicon glyphicon-trash"></span></a></td><td>' + diff + '</td></tr>'
            );
            weightBuff = value[2];
        })
    });
}

function nutritionScripts() {
    $().ready(function () {
        $('#weight-table').on('click', '.remove-weight-btn', function (e) {
            var weightId = $(this).data('weightId');
            e.preventDefault();
            $.ajax({
                type: "DELETE",
                //dataType: "jsonp",
                url: '/api/weight/' + weightId,
                success: function (data) {
                    $(this).parents('tr').fadeOut().remove();
                    console.log(data);
                }
            });
        });
        diff = 0;
        weightBuff = chartData[0][2];
        $.each(chartData, function (index, value) {
            diff = value[2] - weightBuff;
            $('#weight-table').append(
                '<tr><td>' + value[1] + '</td><td>' + value[2] + '</td><td><a href="#" data-weight-id=' + value[0] + ' class="remove-weight-btn"><span class="glyphicon glyphicon-trash"></span></a></td><td>' + diff + '</td></tr>'
            );
            weightBuff = value[2];
        })
    });
}