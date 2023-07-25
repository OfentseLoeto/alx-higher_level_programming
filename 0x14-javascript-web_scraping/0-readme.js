#!/usr/bin/node
'use strict';
const fs = require('fs');

function readFile(filePath) {

  fs.readFile(filePath, 'utf-8', (error, content) => {

    if (error) {
     console.error(error);

  } else {
    console.log(content);
}
});

}

if (process.argv.length !== 3) {
 console.error('Usage: node 0-read_me.js <file_path>');

} else {
  const filePath = process.argv[2];
  readFile(filePath);
}
