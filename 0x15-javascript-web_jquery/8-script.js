const $ = window.$;
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function (data) {
      const movieList = $('#list_movies');
      data.results.forEach(function (movie) {
        const title = $('<li>').text(movie.title);
        movieList.append(title);
      });
    },
    error: function (xhr, status, error) {
      console.error('Error fetching movie title:', error);
    }
  });
});
