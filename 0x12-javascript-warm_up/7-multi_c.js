#!/usr/bin/node

// script that prints x times “C is fun
// If the first argument can’t be converted to an integer,
// print “Missing number of occurrences"

const arg = process.argv[2];

const x = parseInt(arg);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
