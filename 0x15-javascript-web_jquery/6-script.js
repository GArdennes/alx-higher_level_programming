const headerToChange = $('header');
const textToChange = 'New Header!!!';

$('DIV#update_header').click(function () {
  headerToChange.text(textToChange);
});
