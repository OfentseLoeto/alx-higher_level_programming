#!/usr/bin/node
'use strict';
// Script that display the status code of a GET request.

const request = require('request');

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`Code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: 2-statuscode.js <URL>');
} else {
  const url = process.argv[2];
  getStatusCode(url);
}
