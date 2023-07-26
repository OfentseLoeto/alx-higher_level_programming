#!/usr/bin/node
// Script that prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');

function countMovies (apiUrl, characterId) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const movieData = JSON.parse(body);
        const moviesWithCharacter = movieData.results.filter(movie =>
          movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );
        console.log(`${moviesWithCharacter.length}`);
      } else {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
      }
    }
  });
}

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL');
} else {
  const characterId = 18;
  countMovies(apiUrl, characterId);
}
