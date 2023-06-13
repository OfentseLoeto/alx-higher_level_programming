#!/usr/bin/node

// A class Rectangle that defines a rectangle
// Then check if w or h is equal to 0 or not a 
// positive integer, create an empty object

const Rectangle = class {

  constructor (w, h){
    
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {

// Returning an empty object if width or height is invalid
      return {};
    }
    this.width = w;
    this.height = h;
}
};
module.exports = Rectangle;
