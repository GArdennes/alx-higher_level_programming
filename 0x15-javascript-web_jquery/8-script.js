$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const movies = data.results; // Access the 'results' property for the array of movies

      // Iterate through each movie and append its title to the UL#list_movies
      movies.forEach(movie => {
        const titleName = movie.title;
        $('UL#list_movies').append(`<li>${titleName}</li>`);
      });
    });
});
