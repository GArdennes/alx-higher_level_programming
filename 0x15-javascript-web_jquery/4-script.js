const headerToChange = $('header');
headerToChange.addClass('red');

$('DIV#toggle_header').click(function () {
  headerToChange.toggleClass('red green');
});
