$(document).ready(function(){

  cascadingbinary();
  cascadingFilter();
  var initialSelection = ["n", "n", "n"];
  var userSelection = initialSelection.slice(0);
  var optionsChosen = [];
  var optionList = getOptionList();


  /* Actual dynamic filter should do the following
  - Keep track of the current selection
  - Reload every level beyond the current one and default to "n"
  - If "n" is the only possible option for the next level, hide it

  1. Get the option list
  2. Set initial selection
  3. Only show submit button when there's a valid set of options selected

  */
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
});
