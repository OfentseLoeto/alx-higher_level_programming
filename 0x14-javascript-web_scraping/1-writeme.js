#!/usr/bin/node
'use strict';

const fs = require('fs');

function writeFile(filePath, content) {
  fs.writeFile(filePath, content,'utf-8', (error) => {

    if (error) {
      console.error(error);
}
});
}

if (process.argv.length !== 4) {
 console.error('Usage: 1-writeme.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeFile(filePath, content);
}
