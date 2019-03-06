var sliderImageText = [
  ["A great way", "to learn Spanish"],
  ["Have a new", "life experience"],
  ["Immerse yourself", "in Peruvian Culture"],
  ["Make", "new friends"],
]

var counter = 0;

var slider = "";


$(document).ready(function(){
  $(".col-1-3.card").click(function() {
    var link = $(this).find("a");
    window.location = link.attr("href");
  });

  // Slider
  if (document.getElementsByClassName('slider').length > 0) {
    if ($('video').length > 0) {
      console.log("Good");
      $('video').on('ended', function() {
        console.log("Ended!");
        slider = setInterval(swapImages, 8000);
      });
    }
    else {
      slider = setInterval(swapImages, 8000);
    }
    $('a.control').on( "click", control);
  }




  function swapImages(){

        var $active = $('.slider .active');
        if ($('.slider .active').next().length > 0 && ( $('.slider .active').next().is("img") || $('.slider .active').next().is("video"))) {
          var $next = $('.slider .active').next();
        }
        else {
          var $next = $('.slider img:first');
        }
        $active.fadeOut(function(){
          $active.removeClass('active');
          $next.fadeIn().addClass('active');
        });
        if (counter == sliderImageText.length) {
          counter = 0;
        };
        setTimeout(swapText, 400);
        function swapText() {
        $('.slider-title').text(sliderImageText[counter][0]);
        $('.slider-subtitle').text(sliderImageText[counter][1]);
        counter++;
        }
      }

  });
