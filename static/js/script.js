$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.slider').slider();
    $(".dropdown-trigger").dropdown();
      //Count nr. of square classes
  var countSquare = $('.square').length;

  //For each Square found add BG image
  for (i = 0; i < countSquare; i++) {
    var firstImage = $('.square').eq([i]);
    var secondImage = $('.square2').eq([i]);

    var getImage = firstImage.attr('data-image');
    var getImage2 = secondImage.attr('data-image');

    firstImage.css('background-image', 'url(' + getImage + ')');
    secondImage.css('background-image', 'url(' + getImage2 + ')');
  }

});
    $('.datepicker').datepicker({
        format: "dd mmm, yyyy",
        yearRange: [1900,2021],
        changeMonth: true,
        changeYear: true,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('select').formSelect();
  });


