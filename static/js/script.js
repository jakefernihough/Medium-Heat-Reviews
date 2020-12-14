$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"}); // Side navigation
    $('.slider').slider(); //about page slider
    $(".dropdown-trigger").dropdown(); //dropdown on navbar
    $('.datepicker').datepicker({ //release date picker
        format: "dd mmm, yyyy",
        yearRange: [1900,2021],
        changeMonth: true,
        changeYear: true,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    $('select').formSelect().css("color", "white");
  });
 


