#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

function fetchPageContent(url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);

} else { 
  
  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
  
  if (writeError) {
    console.error('Error writing to file:', writeError);
} else {
  console.log(`Webpage content saved to ${filePath}`);
}
});

} else {
  console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
}
}
});
}

const url = process.argv[2];
const filePath = process.argv[4];

if (!url || !filePath) {
  console.error('Provide URL and filePath');

} else {
  fetchPageContent(url, filePath);
}
