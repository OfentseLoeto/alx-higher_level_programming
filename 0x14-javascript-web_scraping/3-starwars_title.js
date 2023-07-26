#!/usr/bin/node
'use strict';
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

function getMovieTitle(movieId) {
 const apiUrl = 'https://swapi-api.alx-tools.com/api/films/:id${movieId}';
 request.get(apiUrl, (error, response, body) => {
 if (error) {
   console.error(error);

} else if (response.statusCode === 200) {
  const movieData = JSON.parse(body);
  console.log(movieData.title);
} else {
  console.error('Error: Failed to get movie with ID ${movieId}. Status code: ${response.statusCode}');
}
});
}

if (process.argv.length !== 3) {
  console.error('(Usage: 3-starwars_title.js <movie_id>');

} else {
  const movieId = process.argv[2];
  getMovieTitle(movieId);
}
