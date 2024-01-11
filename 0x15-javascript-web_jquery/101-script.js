$(function () {
  const listToChange = $('UL.my_list');
  const listToAdd = $('<li>Item</li>');

  $('DIV#add_item').click(function () {
    listToChange.append(listToAdd.clone()); // Use clone() to add a new instance of the element
  });

  $('DIV#remove_item').click(function () {
    listToChange.children('li:last').remove(); // Remove the last li element
  });

  $('DIV#clear_list').click(function () {
    listToChange.empty(); // Remove all child elements inside the UL
  });
});
