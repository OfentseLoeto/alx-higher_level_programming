#!/usr/bin/node

// Script that print addition of two numbers

function add (a, b) {
  console.log(a + b);
}

// parsing command line arguments
const args = process.argv.slice(2);

// check if 2 arguments are passed
if (args.length !== 2) {
  console.log('NaN');
} else {
  const num1 = parseInt(args[0]);
  const num2 = parseInt(args[1]);

  // Check if argument are integers
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    // Calling the add function with the provided integer

    add(num1, num2);
  }
}
