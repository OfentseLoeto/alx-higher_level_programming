#!/usr/bin/node

// Creating a class Rectangle that defines a rectangle
// Then if w or h is equal to 0 or not a positive integer, create an empty object
// And Create an instance method called print()
// that prints the rectangle using the character X

const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // Return an empty object if width or height is invalid
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      console.log('Empty object');
      return;
    }
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    if (Object.keys(this).length === 0) {
      return;
    }
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    if (Object.keys(this).length === 0) {
      return;
    }
    this.width *= 2;
    this.height *= 2;
  }
};
module.exports = Rectangle;
