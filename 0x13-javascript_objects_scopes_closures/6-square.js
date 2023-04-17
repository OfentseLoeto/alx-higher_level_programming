#!/usr/bin/node

// a class Square that defines a square and
// inherits from Square of 5-square.js

const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    const char = c;
    if (c === undefined) {
      c = 'X';
      const row = char.repeat(this.size);
      for (let i = 0; i < this.size; i++) {
        console.log(row);
      }
    }
  }
}
module.exports = Square;
