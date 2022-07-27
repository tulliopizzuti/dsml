function startSpinner(selector){
    var spinnerHtml='<div class="spinner-container text-center m-5""> <div class="spinner-border text-success" role="status"> <span class="visually-hidden">Loading...</span> </div></div>';
    $(selector).children().addClass("d-none")
    $(selector).prepend($(spinnerHtml));
}
function stopSpinner(selector){
    $(selector+" .spinner-container").remove();
    $(selector+ " .d-none").removeClass("d-none")

}