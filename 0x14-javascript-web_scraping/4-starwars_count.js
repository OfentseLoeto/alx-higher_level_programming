#!/usr/bin/node
// Script that prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    const data = JSON.parse(body);
    const characterId = 18;
    const moviesWithWedgeAntilles = data.results.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
