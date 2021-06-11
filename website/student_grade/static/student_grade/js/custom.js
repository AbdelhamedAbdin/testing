$(document).ready(function () {

    let table = $('#table_id').DataTable( {
        responsive: true,
        bPaginate: false,
        paging: false,
        ordering: false,
        info: false,
        bFilter: false
    }).columns.adjust().responsive.recalc();
    new $.fn.dataTable.FixedHeader( table );
})