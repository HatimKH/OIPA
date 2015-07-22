// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

$(document).ready(function(){
    $('nav .tabs a').on('click', function(e){
        e.preventDefault();
        var clickedAnchor = this;
        if (clickedAnchor.pathname == '/api') {
            $('header').slideUp(1000);
            $('#logo').slideDown(1000, function(){
                location.href = clickedAnchor.href;
            });
        }
        else {
            if ( $('header').css('display') == 'none' ){
                $('header').slideDown(1000);
                $('#logo').slideUp(1000, function(){
                    location.href = clickedAnchor.href;
                });
            }
            else {
                location.href = clickedAnchor.href;
            }
        }
    });

});

//  animaties. ff uit.
//  $(window).load(function(){
// 	setTimeout(function () {
//         $('.letter:eq(0)').addClass('animated fadeIn').show();
//     }, 0);
//     setTimeout(function () {
//         $('.letter:eq(1)').addClass('animated fadeIn').show();
//     }, 100);
//     setTimeout(function () {
//         $('.letter:eq(2)').addClass('animated fadeIn').show();
//     }, 200);
//     setTimeout(function () {
//         $('.letter:eq(3)').addClass('animated fadeIn').show();
//         $('.blink').hide();
//     }, 300);
// });