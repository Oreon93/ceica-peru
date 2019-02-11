$(document).ready(function(){

  // Menu functionality
  $("#menu-toggle").click(function(){
    $(this).toggleClass("close");
    $(this).toggleClass("open");
    $(".navbar").toggleClass("show");
    $(".screen").toggleClass("show");
  });

  $(".sub-menu-label").click(function(e) {
    e.stopPropagation();
    e.preventDefault();
    if ($(this).parent().hasClass("opened")) {
      $(".sub-menu-link").removeClass("opened");
    } else {
      $(".sub-menu-link").removeClass("opened");
      $(this).parent().addClass("opened");
    }

  });

  $(".sub-menu-back").click(function(e) {
    e.stopPropagation();
    e.preventDefault();
    if ($(this).parent().parent().parent().hasClass("opened")) {
      $(".sub-menu-link").removeClass("opened");
    } else {
      $(".sub-menu-link").removeClass("opened");
      $(this).parent().parent().parent().addClass("opened");
    }

  });




  radioselect('#id_course_chosen');
  radioselect('#id_current_spanish_level');
  radioselect('#id_accommodation');
  radioselect('#id_accommodation_type');
  radioselect('#id_room_type');
  radioselect('#id_catering');
  radioselect('#id_group_number');
  radioselect('#id_airport_pickup');
  checkboxselect('#id_interested_in');
  ifaccordion();
  iftable();
  date();

  // LANGUAGE NAV
  var current_language = $("#current-language").text();
  var selector = "#" + current_language;
  $(selector).addClass("selected");

  /* Resize text by language */
  if (current_language == "es") {
    console.log("Spanish!");
    $(".primary-nav").addClass("smaller");
  }

  // PRICE LIST
  function iftable() {
    if ($('.price-list').length > 0) {
      $('td:empty').text("n/a");
    }
  }

  // ACCORDIONS
  function ifaccordion() {
    if ($('.accordion').length > 0) {
      console.log("hello!");
      $('.accordion').on("click", function() {
        $(this).toggleClass("active");
        $(this).find("svg").remove();
        if ($(this).hasClass("active")) {
          $(this).append('<i class="fas fa-angle-up fa-lg style="float:right""></i>');
        }
        else {
          $(this).append('<i class="fas fa-angle-down fa-lg style="float:right""></i>');
        }
        var panel = $(this).next();
        $(panel).toggle(duration=400);
      });
    }
  }


// Enroll part 2 - show the "different levels" option only when group number > 1
$("#id_current_spanish_level_3").parent().parent().hide();


$("#id_group_number_1, #id_group_number_2, #id_group_number_3").click(function(e) {
  e.stopPropagation();
  e.preventDefault();
  $("#id_current_spanish_level_3").parent().parent().show();
});

$("#id_group_number_0").click(function(e) {
  e.stopPropagation();
  e.preventDefault();
  $("#id_current_spanish_level_3").parent().parent().hide();
});



function radioselect(id) {
  var id = id;
  /* Load list of options */
  var count = $(id).children().length;
  for (i=0; i<count; i++) {
    var link = id + "_" + i;
    $(link).on("click", function() {
      $(id).find("li").removeClass('answer-selected');
      $(this).parent().parent().addClass('answer-selected');
    });
  }

}

function checkboxselect(id) {
  var id = id;
  /* Load list of options */
  var count = $(id).children().length;
  for (i=0; i<count; i++) {
    var link = id + "_" + i;
    $(link).on("click", function() {
      $(this).parent().parent().toggleClass('answer-selected');
    });
  }

}


  function date() {
    var dateFields = [
      "#id_arrival_date",
      "#id_departure_date",
      "#id_course_start_date"
    ];
    dateFields.forEach(function(field) {
      if($(field).length) {
        $(field).datepicker(
          {
            dateFormat: "dd/mm/yy"
          }
        );
      }
    });
  }
});
