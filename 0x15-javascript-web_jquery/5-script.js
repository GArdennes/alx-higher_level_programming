const listToChange = $('UL.my_list');
const listToAdd = $('<li>Item</li>');

$('DIV#add_item').click(function () {
  listToChange.append(listToAdd);
});
