#!/usr/bin/node
'use strict';
// This script that display the status code of a GET request.

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node get-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
