$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const characterName = data.name;
      $('DIV#character').text(characterName);
    });
});
