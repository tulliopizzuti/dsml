$(document).ready(function(){
    setMenu();
});

function setMenu(){
    var menu=$('head meta[name="menu"]').attr("value");
    if(menu){
        $('#'+menu).addClass("active");
    }
}