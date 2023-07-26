#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

function getMovieTitleById (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const movieData = JSON.parse(body);
        console.log(`${movieData.title}`);
      } else {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
      }
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
} else {
  getMovieTitleById(movieId);
}
