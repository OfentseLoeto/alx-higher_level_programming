#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error('Error:', writeError.message);
      } else {
        console.log(filePath);
      }
    });
  }
});
