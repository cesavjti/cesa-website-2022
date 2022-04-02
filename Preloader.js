$(document).ready(function(){   
        window.setTimeout('fadeout();', 3000);
        
    });

    function fadeout(){
        $('#Preloader').delay(2000).fadeOut('slow', function() {
           $('.notLoaded').removeClass('notLoaded');
        });
    }