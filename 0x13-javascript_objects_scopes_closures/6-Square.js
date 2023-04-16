#!/usr/bin/node

// a class Square that defines a square and
// inherits from Square of 5-square.js

const SquareP = require('./5-square');

class Square extends SquareP {
    charPrint (c) {
   if ( c === undefined) {
      c = 'X';
   }
      let row = '';
   for (let i = 0; i < this.width; i++) {
     row += 'c';
   }
   for (let j = 0; j < this.height; j++) {
     console.log(row);
   }
    }
}
module.exports = Square;
