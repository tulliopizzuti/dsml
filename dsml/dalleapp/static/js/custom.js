$(document).ready(function () {
    setMenu();
    //setClickableTableRow();
});

function setMenu() {
    var menu = $('head meta[name="menu"]').attr("value");
    if (menu) {
        $('#' + menu).addClass("active");
    }
}
/*function setClickableTableRow(){
    $("table.clickable tr[data-href]").on("click",function () {
        console.log("click");
        window.location = $(this).data("href");
    });
}*/