var sliderImageText = [
  ["A great way", "to learn Spanish"],
  ["Have a new", "life experience"],
  ["Immerse yourself", "in Peruvian Culture"],
  ["Make", "new friends"],
]

var counter = 0;
var secondcounter = 0;
var slider = "";
var testimonials = "";


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
  if (document.getElementsByClassName('quote').length > 0) {
    $('.quote:first').addClass("current");
    testimonials = setInterval(swapTestimonials, 8000);
    $('a.control').on( "click", control);
  }

  // Testimonials
  function control() {
    clearInterval(testimonials);
    console.log("Yay");
    if ($(this).hasClass('control-left')) {
      rewindTestimonials();
    }
    else {
      swapTestimonials();
    }
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

  function swapTestimonials(){
    secondcounter++;
    var $active = $('.quote.current');
    if ($('.quote.current').next().length > 0 && $('.quote.current').next().is("div")) {
      var $next = $('.quote.current').next();
    }
    else {
      var $next = $('.quote:first');
    }
    $active.fadeOut(function(){
      $active.removeClass('current');
      $next.removeAttr('style');
      $next.addClass('current');
    });
    console.log("swap!");
  }

  function rewindTestimonials(){
    var $active = $('.quote.current');
    if ($('.quote.current').prev().length > 0 && $('.quote.current').prev().is("div")) {
      var $prev = $('.quote.current').prev();
    }
    else {
      var $prev = $('.quote:last');
    }
    $active.fadeOut(function(){
    $active.removeClass('current');
    $prev.removeAttr('style');
    $prev.addClass('current');
    });
    console.log("rewind!");
  }

});
