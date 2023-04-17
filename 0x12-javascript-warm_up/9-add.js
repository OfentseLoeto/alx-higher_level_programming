#!/usr/bin/node

// script that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer
// You have to define a function with this prototype: function add(a, b)

function add (a, b) {
  return a + b;
}
if (process.argv.length < 4) {
  console.log(NaN);
} else {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}
