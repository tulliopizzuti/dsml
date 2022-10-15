function startSpinner(selector){
    var spinnerHtml='<div class="spinner-container text-center m-5""> <div style="width: 3rem; height: 3rem;" class="spinner-grow text-primary" role="status"> <span class="visually-hidden">Loading...</span> </div></div>';
    var overlay='<div id="overlay" class="d-flex flex-column align-items-center justify-content-center"></div>';
    var timer='<div id="timer">00:00:00</div>'
    if(selector){
        $(selector).children().addClass("d-none");
        $(selector).prepend($(spinnerHtml));
    }
    else{

        $("body").prepend($(overlay));
        $("#overlay").append(spinnerHtml);
        $("#overlay").append(timer);

        var timer =new  easytimer.Timer();
        timer.start();
        timer.addEventListener('secondsUpdated', function (e) {
            $('#timer').html(timer.getTimeValues().toString());
        });
    }
    
}
function stopSpinner(selector){
    if(selector){
        $(selector+" .spinner-container").remove();
        $(selector+ " .d-none").removeClass("d-none");
    }
    else{
        $("#overlay").remove();
    }


}