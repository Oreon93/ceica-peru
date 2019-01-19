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
  var  score = 0;

  radioselect('#id_course_chosen');
  radioselect('#id_current_spanish_level');
  radioselect('#id_accommodation');
  radioselect('#id_accommodation_type');
  radioselect('#id_room_type');
  radioselect('#id_catering');
  radioselect('#id_airport_pickup');
  checkboxselect('#id_interested_in');
  //dynamicview();
  cascadingbinary();
  cascadingFilter();
  ifaccordion();
  iftable();
  date();

  // LANGUAGE NAV
  var current_language = $("#current-language").text();
  var selector = "#" + current_language + " img";
  $(selector).addClass("active-language");


  // STICKY NAVBAR
  var navbar = document.getElementById("scroll-nav");
  var sticky = navbar.offsetTop;
  console.log(navbar.offsetTop);
  window.onscroll = function() {stickyNavBar()};

  function stickyNavBar() {
    if (window.pageYOffset >= sticky+40) {
      $('#scroll-nav ul').addClass("sticky-ul");
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
      $('#scroll-nav ul').removeClass("sticky-ul");
    }
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

/* Actual dynamic filter should do the following
- Keep track of the current selection
- Reload every level beyond the current one and default to "n"
- If "n" is the only possible option for the next level, hide it

1. Get the option list
2. Set initial selection
3. Only show submit button when there's a valid set of options selected

*/


var initialSelection = ["n", "n", "n"];
var userSelection = initialSelection.slice(0);
var optionsChosen = [];
var optionList = getOptionList();

function cascadingbinary() {
  $('.cascading-binary input').on("click", function() {
    var value = $(this).val();
    if (value == "y") {
      userSelection = ["h", "n", "n"];
      $("#submit").hide();
      $("#level-0").show();
      $("#level-0 li").addClass("validoption");
      submitDisplay(userSelection, optionList);
    } else{
      optionsChosen = [];
      userSelection = initialSelection.slice(0);
      $("#level-0").hide();
      hideExtraLevels();
      submitDisplay(userSelection, optionList);
    }

  })
};

function cascadingFilter() {
  $('.cascading input').on("click", function() {
    var value        = $(this).val(),
        container    = $(this).parent().parent().parent().parent(),
        currentLevel = parseInt(container.attr("id").slice(6));

    //Update selection, filter relevant options, then render!
    trackSelection(value, currentLevel, function() {
      filterOptions(currentLevel, optionList, function(options) {
        renderOptions(options);
      });
    });
  });
};

function trackSelection(value, currentLevel, next) {
  userSelection[currentLevel] = value;
  optionsChosen = userSelection.slice(0, currentLevel + 1);
  next();
}

function filterOptions(currentLevel, optionList, next) {
  // Get options
  var filteredOptionList = optionList.filter(function (option) {
    var i = 0;
    while (i<optionsChosen.length) {
      if (option[i] != optionsChosen[i]) {
        return false;
      }
      i++;
    }
    return true;
  })

  // Work out the options at the next level
  var visibleOptions = [];
  var thisLevel =  filteredOptionList.map(function(optionSet) {
      return optionSet[currentLevel+1];
    });
  visibleOptions = Array.from(new Set(thisLevel));
  console.log(visibleOptions);

  //Then render up to the "next level" beyond what the user has so far selected
  next(visibleOptions);
}

function renderOptions(uniqueNextOptions) {
  hideExtraLevels();

  // Refresh and show next set of options
  var nextLevel = optionsChosen.length;
  $("#level-" + nextLevel + " input").parent().parent().removeClass('validoption');
    $("#level-" + nextLevel + " input").parent().parent().removeClass('answer-selected');
  $("#level-" + nextLevel).show();
  uniqueNextOptions.forEach(function(option) {
    var optionBox = "#level-"+nextLevel+" input[value='"+option +"']";
    console.log(optionBox);
    $(optionBox).parent().parent().addClass('validoption');
  });

  // Show or hide submit
  submitDisplay(userSelection, optionList);
}

function hideExtraLevels() {
  // Hide levels beyond the next options
  for (var i=optionsChosen.length + 1; i < userSelection.length; i++ ) {
    $("#level-"+i).hide();
  };
}

function getOptionList() {
  list = (document.getElementById('optionlist').innerHTML.trim());
  array = list.split(",");
  list = array.filter( function( element ) {
    return element.length > 0;
  });
  for (i=0; i<list.length; i++) {
    list[i] = list[i].split(" ");
  }
  return list;
};

function submitDisplay(userSelection, optionList) {
  if (JSON.stringify(userSelection) == JSON.stringify(initialSelection)) {
    // Show submit button
    console.log("display submit!");
    $("#submit").show();
  } else {

    // See if user has selected valid accommodation options - aka "completed" the form
    var cs = JSON.stringify(userSelection);
    var ol = JSON.stringify(optionList);
    console.log(cs);
    console.log(ol);
    // Check if user has a valid option set and has made all the choices available
    if (ol.indexOf(cs) !== -1 && optionsChosen.length == userSelection.length) {
      // Show submit button
      $("#submit").show();

      // Record selection!!!
      $("#id_accommodation_choice").val(JSON.stringify(userSelection));
      console.log(userSelection);
    } else {
      // Hide submit button
      $("#submit").hide();
    }
  }
}

/*
function dynamicview() {
  $('.cascading input').on("click", function() {
      var value = $(this).val();
      container = $(this).parent().parent().parent().parent();
      container.next().removeClass('dynamic-options');
      var container_id = container.attr("id");
      if (container_id !== undefined) {
      currentlevel = parseInt(container.attr("id").slice(6));
      trackselection(currentlevel, value);
      }
    })
  };
*/


function trackselection(currentlevel, value) {
  current_selection[currentlevel] = value;
  if (current_selection.length > currentlevel +1) {
    for (i = current_selection.length; i > currentlevel +1; i--) {
      current_selection.pop();
    }
  }
  console.log(current_selection);
  optionfilter(currentlevel);
  /*filteroptions(currentlevel)*/;

}

function optionfilter(currentlevel) {
  /* Get inputs of next optionset */
  var div_name = "level-" + (currentlevel+1);
  console.log("hello?");
  var container = $('#'+div_name);
  var input = $('#'+div_name).find("input");
  console.log(input);

  /* Avoid additive filtering! */
  $(input).parent().parent().removeClass('validoption');


  var filteredOptionList = optionlist.slice(0);

  /* Filter the accommodation options by the current selection */
  var filter = current_selection;
  filteredOptionList = filteredOptionList.filter(function (option) {
    var i = 0;
    while (i<current_selection.length) {
      if (option[i] != filter[i]) {
        return false;
      }
      i++;
    }
    return true;
  });


  /* Now filter out inputs that don't match the remaining options */
  for (i = 0; i<filteredOptionList.length; i++) {
    for (j = 0; j< input.length; j++) {
      var this_input = input[j];
      var input_value = $(this_input).val();
      if (filteredOptionList[i][currentlevel + 1] == input_value) {
        $(this_input).parent().parent().addClass('validoption');
      }
    }
  }
}


/* Simple function to reveal the next set of options.
function cascadingbinary() {
  $('.cascading-binary input').on("click", function() {
    var value = $(this).val();
    container = $(this).parent().parent().parent().parent();
    if (value != "n") {
      container.next().removeClass('dynamic-options');
      container.next().find('li').addClass('validoption');
    }
    else {
      container.next().addClass('dynamic-options');
      container.next().next().addClass('dynamic-options');
      container.next().next().next().addClass('dynamic-options');
    }
  })
};
*/


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
    console.log("DATE");
    $("#id_arrival_date").datepicker();
    $("#id_departure_date").datepicker();
    console.log("DATE");
}






/* Deprecated option filter
function filteroptions(currentlevel) {
  var div_name = "level-" + (currentlevel+1);
  var container = $('#'+div_name);
  var input = $('#'+div_name).find("input");
  for (i = 0; i< input.length; i++) {
    var this_input = input[i];
    var input_value = $(this_input).val();
    console.log(input_value + "is the input we're filtering");
    score = 0;
    recursivefilter(currentlevel, input_value);
    if (score == 0)
      {
        $(this_input).parent().parent().hide();
      }
  }
}

function recursivefilter(currentlevel, input_value) {
  console.log('the current level is' + currentlevel)
  for (j = 0; j<optionlist.length; j++) {
    console.log("input:"+ input_value+ ", tocheckagainst:" +optionlist[j][currentlevel]);
    if (optionlist[j][currentlevel] == input_value) {
      console.log("Right");
      if (currentlevel == 0) {
        score += 1;
        console.log(score);
      }
      else {
      console.log(score);
      recursivefilter(currentlevel - 1, current_selection[currentlevel])
      }
    }
  }
}
*/




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
